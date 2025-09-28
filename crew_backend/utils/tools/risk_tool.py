from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import re

class RiskInput(BaseModel):
    """Input schema for RiskTool."""

    financial_document_data: str = Field(..., description="Extracted text from a risk-related financial document")

## Creating Risk Assessment Tool
class RiskTool(BaseTool):
    name: str = "RiskAnalyzer"
    description: str = "Analyzes financial documents and provides risk assessment."
    args_schema: Type[BaseModel] = RiskInput

    def _run(self, financial_document_data: str) -> str:        
        # TODO: Implement risk assessment logic here
        # --- Step 1: Clean up text ---
        processed_data = re.sub(r"\s+", " ", financial_document_data.strip())

        # --- Step 2: Define risk keywords ---
        high_risk_keywords = [
            "bankruptcy", "default", "lawsuit", "litigation", "volatility",
            "loss", "decline", "restructuring", "fraud", "regulatory risk"
        ]
        medium_risk_keywords = [
            "debt", "uncertainty", "downgrade", "warning", "delayed", "instability"
        ]

        # --- Step 3: Count risk signals ---
        high_risk_hits = [word for word in high_risk_keywords if re.search(rf"\b{re.escape(word)}\b", processed_data, re.I)]
        medium_risk_hits = [word for word in medium_risk_keywords if re.search(rf"\b{re.escape(word)}\b", processed_data, re.I)]

        # --- Step 4: Compute risk score ---
        risk_score = len(high_risk_hits) * 2 + len(medium_risk_hits)
        if risk_score >= 4:
            risk_level = "HIGH"
            recommendation = "Immediate review and caution required. Consider hedging or avoiding exposure."
        elif risk_score >= 2:
            risk_level = "MEDIUM"
            recommendation = "Moderate risk. Monitor the situation and manage exposures carefully."
        else:
            risk_level = "LOW"
            recommendation = "Low risk detected. Proceed normally, but stay vigilant."

        # --- Step 5: Build a readable report ---
        report_lines = []
        report_lines.append("⚠️ **Financial Risk Assessment Report**")
        report_lines.append(f"Risk Score: {risk_score}")
        if high_risk_hits:
            report_lines.append(f"High Risk Signals Detected: {', '.join(high_risk_hits)}")
        if medium_risk_hits:
            report_lines.append(f"Medium Risk Signals Detected: {', '.join(medium_risk_hits)}")
        report_lines.append(f"Overall Risk Level: **{risk_level}**")
        report_lines.append(f"Recommendation: {recommendation}")
        report_lines.append("Disclaimer: This is heuristic-based analysis, not professional financial advice.")

        return "\n".join(report_lines)
        # return "Risk assessment functionality to be implemented"