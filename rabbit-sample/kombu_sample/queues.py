from kombu import Exchange, Queue

task_exchange = Exchange("kombu_demo", type="direct")
task_queues = [Queue("kombu_demo", task_exchange, routing_key="kombu_demo")]
