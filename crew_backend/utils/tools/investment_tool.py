from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import re

class InvestmentInput(BaseModel):
    """Input schema for InvestmentTool."""

    financial_document_data: str = Field(..., description="Extracted text from a financial document")

## Creating Investment Analysis Tool
class InvestmentTool(BaseTool):
    name: str = "InvestmentAnalyzer"
    description: str = "Analyzes financial documents and provides investment advice."
    args_schema: Type[BaseModel] = InvestmentInput

    def _run(self, financial_document_data: str) -> str:
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        # --- Step 1: Preprocess data ---
        processed_data = re.sub(r"\s+", " ", financial_document_data.strip())

        # --- Step 2: Basic keyword-based sentiment analysis ---
        positive_keywords = ["growth", "increase", "profit", "record high", "strong", "surplus", "beat expectations"]
        negative_keywords = ["loss", "decline", "drop", "decrease", "deficit", "missed expectations", "bankruptcy"]

        pos_hits = [word for word in positive_keywords if re.search(rf"\b{re.escape(word)}\b", processed_data, re.I)]
        neg_hits = [word for word in negative_keywords if re.search(rf"\b{re.escape(word)}\b", processed_data, re.I)]

        sentiment_score = len(pos_hits) - len(neg_hits)

        # --- Step 3: Generate heuristic investment advice ---
        if sentiment_score > 2:
            recommendation = "BUY - strong bullish indicators detected."
            confidence = "High"
        elif sentiment_score > 0:
            recommendation = "ACCUMULATE - moderate positive signals, good for long-term investors."
            confidence = "Medium"
        elif sentiment_score == 0:
            recommendation = "HOLD - market appears neutral, wait for more data."
            confidence = "Low"
        else:
            recommendation = "SELL - bearish signals detected, risk is elevated."
            confidence = "High"

        # --- Step 4: Extract basic financial numbers (optional) ---
        revenue_match = re.search(r"revenue[^0-9]*([\d,.]+)", processed_data, re.I)
        profit_match = re.search(r"(?:profit|net income)[^0-9]*([\d,.]+)", processed_data, re.I)

        # --- Step 5: Build final report ---
        report_lines = []
        report_lines.append("📊 **Investment Analysis Report**")
        report_lines.append(f"Sentiment Score: {sentiment_score} (Pos: {len(pos_hits)}, Neg: {len(neg_hits)})")
        if revenue_match:
            report_lines.append(f"Revenue Mentioned: {revenue_match.group(1)}")
        if profit_match:
            report_lines.append(f"Profit Mentioned: {profit_match.group(1)}")
        if pos_hits:
            report_lines.append(f"Positive Signals: {', '.join(pos_hits)}")
        if neg_hits:
            report_lines.append(f"Negative Signals: {', '.join(neg_hits)}")
        report_lines.append(f"\n💡 Recommendation: **{recommendation}** (Confidence: {confidence})")
        report_lines.append("⚠️ Disclaimer: This is heuristic-based analysis and not financial advice.")

        return "\n".join(report_lines)

        # return "Investment analysis functionality to be implemented"
