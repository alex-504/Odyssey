import socket

api_key = "53aa470f-aee1-4225-8bc6-4ad633f71404"
try:
     conn = socket.create_connection((f"{api_key}.carbon.hostedgraphite.com", 2003))
     conn.send(f"{api_key}.flask_app.test_metric 1\n".encode('utf-8'))
     conn.close()
     print("Metric sent successfully!")
except Exception as e:
    print(f"Failed to send metric: {e}")
    print(traceback.format_exc())
