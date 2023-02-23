from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://55ahi2jxmrvrg4br7yto:pscale_pw_eFRilOYul8nq6AXnsCZF2fJj3u4bnc0f6MN9NKTW4jf@ap-northeast.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }   
  })

