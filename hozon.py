def hozon(text: str) -> str:
    """文字起こししたテキストをhozon.txtに追記する。

    Args:
        text (str): 保存する文字起こしデータ

    Returns:
        str: 保存先のファイル名
    """
    with open("hozon.txt", "a", encoding="utf-8") as file:#aは追記モード
        file.write(text + "\n")

    return "hozon.txt"