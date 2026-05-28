import mlflow

mlflow.set_experiment("LLMOps Monitoring")

with mlflow.start_run():

    mlflow.log_metric("rouge_score", 0.88)
    mlflow.log_metric("latency", 120)
