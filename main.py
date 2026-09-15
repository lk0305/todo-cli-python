"""A simple command-line entry point for the todo application."""

import json


def display_menu() -> None:
    """Print the available todo actions."""
    print("\n请选择操作：")
    print("1. 查看待办")
    print("2. 添加待办")
    print("3. 退出")


def main() -> None:
    """Run the interactive menu."""
    try:
        with open("todos.json", "r", encoding="utf-8") as file:
            todos = json.load(file)
    except IOError:
        todos = []

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
            if not todos:
                print("暂无待办事项。")
            else:
                for index,todo in enumerate(todos,start=1):
                    print("{}.{}".format(index,todo))
        elif choice == "2":
            todo = input("请输入待办事项:").strip()
            todos.append(todo)
            with open("todos.json", "w", encoding="utf-8") as file:
                json.dump(todos, file, ensure_ascii=False, indent=2)
            print("添加成功")
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()