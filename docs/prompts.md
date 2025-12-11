# AI Prompts Documentation

## Overview

This document describes the AI prompts used in the intake system for processing client enquiries.

**Current Status**: PHASE 2 (AI analysis implemented - data capture + LLM processing)

## Intake Filter Prompt

**Purpose**: Analyze raw text from IntakeSession and generate structured data for filtering and routing.

**Status**: ✅ IMPLEMENTED (PHASE 2)

**Implementation Details**:
- System prompt stored in: `ai/prompts/intake_prompt.txt`
- Triggered by owner via: `/owner/intake/<uuid>/analyse/` (POST)
- Uses shared LLM helper: `pages/llm_utils.call_llm_json()`
- Results stored in: `IntakeSession.structured_output` (JSONField)
- View implementation: `pages/views.owner_intake_analyse()`

### Expected Input

- `raw_text`: Free-text description of the client's matter from the intake form
- `name`: Optional client name
- `email`: Optional client email

### Expected Output (JSON)

The AI will generate a JSON object stored in `IntakeSession.structured_output` with the following structure:

```json
{
  "case_type": "string",           // e.g., "employment", "commercial", "regulatory", "personal_injury"
  "urgency": "string",              // "low", "medium", "high", "emergency"
  "timeline": "string",             // Description of relevant deadlines or time pressures
  "missing_info": ["string"],       // Array of information gaps that need clarification
  "suitability": "boolean",         // Whether this appears suitable for the barrister's practice
  "recommended_consultation_type": "string",  // "initial", "followup", "urgent"
  "risk_flags": ["string"],         // Array of potential issues (e.g., ["conflict_of_interest", "out_of_jurisdiction"])
  "summary": "string",              // 2-3 sentence executive summary
  "confidence": "number"            // 0.0 to 1.0 confidence score in the analysis
}
```

### Production Prompt

The full production prompt is stored in `ai/prompts/intake_prompt.txt` and includes:

**Key Features**:
- 10 predefined case type categories (employment, commercial, regulatory, etc.)
- 4 urgency levels (emergency, high, medium, low)
- 8 risk flag types (conflict_of_interest, urgent_deadline, vexatious, etc.)
- Conservative assessment guidelines (flag for review when uncertain)
- Detailed examples and instructions
- Strict JSON output format enforcement

**Prompt Structure**:
1. Role definition and critical rules
2. Case type taxonomy
3. Urgency level definitions
4. Consultation type recommendations
5. Risk flag catalog
6. Suitability assessment guidelines
7. Missing information examples
8. JSON output schema
9. Example input/output pair

See `ai/prompts/intake_prompt.txt` for the complete production prompt (90 lines).

## Summary Prompt

**Purpose**: Generate a concise summary of the enquiry for quick owner review.

**Status**: Not yet implemented (PHASE 2)

### Expected Output

2-3 sentence executive summary suitable for display in the owner dashboard list view.

## Risk Tagger Prompt

**Purpose**: Identify potential red flags or issues that require immediate attention.

**Status**: Not yet implemented (PHASE 2)

### Risk Categories

- **Conflict of Interest**: Potential conflicts with existing clients
- **Out of Jurisdiction**: Matter outside barrister's practice area or geographical scope
- **Urgent Deadline**: Time-sensitive matter requiring immediate attention
- **Unsuitable Matter**: Type of case the barrister doesn't handle
- **Incomplete Information**: Critical missing details
- **Vexatious**: Signs of frivolous or vexatious enquiry

## Implementation Notes

### PHASE 2 Completed ✅

1. ✅ Finalized intake filter prompt template (`ai/prompts/intake_prompt.txt`)
2. ✅ Implemented LLM API integration via shared helper (`pages/llm_utils.py`)
3. ✅ Created owner interface for triggering and reviewing AI output
4. ✅ Added structured data display in detail view
5. ✅ Implemented error handling for LLM failures
6. ✅ Added AI status indicators in list view

### PHASE 3 Tasks (Future)

1. Add background task processing (Celery or similar) for automatic analysis
2. Add manual override capabilities (edit AI results)
3. Implement comprehensive logging and audit trail
4. Add filtering by AI results (suitability, case type, urgency)
5. Email notifications based on AI assessment

### Testing Strategy

- Start with sample enquiries
- Compare AI output against manual assessment
- Iterate on prompts based on accuracy
- Establish confidence thresholds for auto-routing vs. manual review

### Privacy & Security

- Ensure client data is handled according to GDPR
- Log all AI processing for audit purposes
- Allow opt-out of AI processing
- Clear data retention policies
- No sensitive data sent to external LLM without encryption

## Prompt Storage

Actual prompt text files will be stored in `/ai/prompts/`:

- `intake_prompt.txt` - Main intake filter prompt
- `summary_prompt.txt` - Case summary generation
- `risk_prompt.txt` - Risk assessment prompt

These files should be version controlled and reviewed before production deployment.
