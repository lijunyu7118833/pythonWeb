
from flask_cors import CORS
import www

from application import app, manager
from flask_script import Server


manager.add_command("runserver",
                    Server(port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))

def main():
    CORS(app, supports_credentials=True)
    manager.run()

if __name__ == '__main__':
    try:
        CORS(app, supports_credentials=True)
        import sys

        # 执行main方法
        sys.exit(main())
    except Exception as e:
        import traceback

        # 打印所有的异常
        traceback.print_exc()

