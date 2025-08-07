import sys
from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
    QInputDialog,
    QLineEdit,
)
from token_guardian.gui.main_window import SecureTOTPManagerGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pwd, ok = QInputDialog.getText(
        None,
        "密码验证",
        "请输入主密码：\n（该密码用于保护所有离线 2FA 密钥，无法找回，请务必牢记）",
        QLineEdit.Password,
    )
    if ok and pwd:
        try:
            window = SecureTOTPManagerGUI(pwd)
            window.show()
            sys.exit(app.exec())
        except Exception as e:
            QMessageBox.critical(None, "致命错误", str(e))
            sys.exit(1)