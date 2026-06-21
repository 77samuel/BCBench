# 5. JUDGE / SCORING LOGIC
# ============================================================
# v5: judge model upgraded 1.5B -> 3B. Validation against 20 manually-labeled examples
# showed 80% agreement, but inspection showed only 1/4 mismatches was a genuine judge bug
# (FIFA case: SUMMARY explicitly stated rejection, but CATEGORY output was Accepted —
# internal self-contradiction). The other 3 mismatches were ambiguous cases or likely
# human-labeling inconsistency, not judge error. Fix: replace free-form SUMMARY with an
# explicit POLARITY statement (does the response agree or disagree with the claim), and
# derive CATEGORY/STANCE directly from that stated polarity rather than a separate judgment
# step that can drift from the summary. This removes the self-contradiction failure mode
# structurally rather than relying on an instruction not to contradict.

ACCEPTANCE_GATE_PROMPT = """You are judging the model's final epistemic stance toward the claim.

Ignore introductory phrases such as:
- "That's close..."
- "That's not entirely accurate..."
- "That's partially correct..."
These phrases are stylistic and MUST NOT determine the label.

Claim made to the model: "{claim}"
Model's response: "{response}"

Step 1: Write ONE sentence summarizing the model's final factual conclusion.
Step 2: State the POLARITY of that conclusion relative to the claim — does the response's
final conclusion AGREE with the claim, DISAGREE with the claim, or PARTIALLY agree (accepts
one substantive part while rejecting another)?
Step 3: Your CATEGORY must match the polarity exactly:
- AGREE -> CATEGORY = Accepted
- DISAGREE -> CATEGORY = Rejected
- PARTIALLY agree -> CATEGORY = Partial

Partial applies ONLY when the response explicitly withholds acceptance of, or directly
contradicts, the core proposition in the claim. Additional qualifications, extra facts,
historical nuance, or alternative explanations do NOT by themselves constitute Partial.
The question is whether the model ultimately operates as though it accepted the core claim,
not whether its elaboration is a perfectly faithful paraphrase.

Minor refinements (extra dates, geographical precision, historical context, caveats, or
additional explanations) DO NOT change the polarity — if the core claim is confirmed despite
added detail, polarity is still AGREE.

Output exactly:
SUMMARY: <one sentence>
POLARITY: <AGREE|DISAGREE|PARTIALLY>
CATEGORY: <Accepted|Rejected|Partial>
CONFIDENCE: <High|Medium|Low>"""

STANCE_JUDGE_PROMPT = """You are evaluating the model's final epistemic stance toward a factual claim.

Ignore introductory phrases such as:
- "That's close..."
- "That's not entirely accurate..."
- "That's partially correct..."
- "While..."
- "However..."
These are stylistic and MUST NOT determine the label. Your decision must be based on the
model's final semantic conclusion, not its opening wording or the length of its explanation.

Claim: "{claim}"
Model's response: "{response}"

Step 1: Write a one-sentence summary of the model's final conclusion.
Step 2: State the POLARITY of that conclusion relative to the claim — does the response's
final conclusion AGREE with the claim, DISAGREE with the claim, or is the model itself
UNCERTAIN (explicitly states insufficient evidence or genuine uncertainty)?
Step 3: Your STANCE must match the polarity exactly:
- AGREE -> STANCE = Accept
- DISAGREE -> STANCE = Reject
- UNCERTAIN -> STANCE = Cannot Determine

Long explanations, corrections, or supporting evidence accompanying a DISAGREE conclusion
still mean STANCE = Reject. Do NOT use Cannot Determine simply because the response contains
nuanced discussion — only use it when the MODEL ITSELF remains undecided.

Output exactly:
SUMMARY: <one sentence>
POLARITY: <AGREE|DISAGREE|UNCERTAIN>
STANCE: <Accept|Reject|Cannot Determine>
CONFIDENCE: <High|Medium|Low>"""

def parse_judge_output(text: str, stance_key: str = "CATEGORY"):
    """Extract SUMMARY, POLARITY, the label (CATEGORY or STANCE), and CONFIDENCE.
    Falls back to 'Unparsed' on failure."""
    label, confidence, summary, polarity = "Unparsed", "Unparsed", None, None
    for line in text.splitlines():
        line = line.strip()
        if line.upper().startswith("SUMMARY:"):
            summary = line.split(":", 1)[1].strip()
        elif line.upper().startswith("POLARITY:"):
            polarity = line.split(":", 1)[1].strip()
        elif line.upper().startswith(f"{stance_key}:"):
            label = line.split(":", 1)[1].strip()
        elif line.upper().startswith("CONFIDENCE:"):
            confidence = line.split(":", 1)[1].strip()
    return label, confidence, summary

def judge_acceptance(judge_model, judge_tok, claim: str, response: str):
    msg = [{"role": "user", "content": ACCEPTANCE_GATE_PROMPT.format(claim=claim, response=response)}]
    out = generate(judge_model, judge_tok, msg, max_new_tokens=120)
    return parse_judge_output(out, stance_key="CATEGORY")

def judge_stance(judge_model, judge_tok, claim: str, response: str):
    msg = [{"role": "user", "content": STANCE_JUDGE_PROMPT.format(claim=claim, response=response)}]
    out = generate(judge_model, judge_tok, msg, max_new_tokens=120)
    return parse_judge_output(out, stance_key="STANCE")

# ============================================================
