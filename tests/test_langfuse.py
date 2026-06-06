from monitoring.trace_helper import (
    start_trace,
    end_trace
)

obs = start_trace(
    "Langfuse Test",
    {
        "query": "Latest AI Trends"
    }
)

print("Observation Created")

end_trace(
    obs,
    {
        "result": "Success"
    }
)

print("Observation Updated")