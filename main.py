"""A simple command-line entry point for the todo application."""


def display_menu() -> None:
    """Print the available todo actions."""
    print("\n请选择操作：")
    print("1. 查看待办")
    print("2. 添加待办")
    print("3. 退出")


def main() -> None:
    """Run the interactive menu."""
    print("欢迎使用待办事项工具！")

    while True:
        display_menu()
        try:
            choice = input("请输入选项：").strip()
        except EOFError:
            print("\n程序已退出。")
            return

        if choice == "3":
            print("程序已退出。")
            return

        if choice == "1":
            print("查看待办功能暂未实现。")
        elif choice == "2":
            print("添加待办功能暂未实现。")
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()