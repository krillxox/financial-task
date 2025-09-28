from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from utils.agents.financial_agent import financial_analyst
from utils.agents.investment_agent import investment_advisor
from utils.agents.risk_agent import risk_assessor
from utils.tasks.financial import financial_task
from utils.tasks.investment import investment_analysis
from utils.tasks.risk import risk_assessment

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str="data/sample.pdf"):
    """To run the whole crew"""
    financial_crew = Crew(
        agents=[financial_analyst, investment_advisor, risk_assessor],
        tasks=[financial_task, investment_analysis, risk_assessment],
        process=Process.sequential,
        config=None,
        verbose=True,
    )
    result = financial_crew.kickoff({'query': query, "path": file_path})
    return result

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document(
    # file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    file_id = str(uuid.uuid4())
    # file_path = f"data/financial_document_{file_id}.pdf"
    print(os.getcwd())
    file_path = "./data/TSLA-Q2-2025-Update.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        # with open(file_path, "wb") as f:
        #     content = await f.read()
        #     f.write(content)
        
        # Validate query
        if query=="" or query is None:
            query = "Analyze this financial document for investment insights"
            
        # Process the financial document with all analysts
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            # "file_processed": file.filename
        }
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)