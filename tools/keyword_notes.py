from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    description: str
    url: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted_summary(self) -> str:
        lines = [
            f"关键词：{self.keyword}",
            f"描述：{self.description}",
            f"关联网址：{self.url}",
            f"标签：{', '.join(self.tags) if self.tags else '无'}",
            f"创建时间：{self.created_at}",
        ]
        return "\n".join(lines)


def batch_print_notes(notes: List[KeywordNote]) -> None:
    for i, note in enumerate(notes, 1):
        print(f"--- 笔记 {i} ---")
        print(note.formatted_summary())
        print()


def export_notes_to_markdown(notes: List[KeywordNote], filename: str = "keyword_notes.md") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 关键词笔记\n\n")
        for i, note in enumerate(notes, 1):
            f.write(f"## 笔记 {i}: {note.keyword}\n\n")
            f.write(f"- **关键词**: {note.keyword}\n")
            f.write(f"- **描述**: {note.description}\n")
            f.write(f"- **关联网址**: {note.url}\n")
            f.write(f"- **标签**: {', '.join(note.tags) if note.tags else '无'}\n")
            f.write(f"- **创建时间**: {note.created_at}\n\n")


def create_sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="爱游戏",
            description="一个专注于家庭娱乐和互动游戏的平台，提供多种休闲游戏体验。",
            url="https://m-home-i-game.com.cn",
            tags=["游戏", "娱乐", "家庭"],
        ),
        KeywordNote(
            keyword="爱游戏 - 热门推荐",
            description="本站精选每日最受欢迎的游戏，涵盖益智、动作、策略等多种类型。",
            url="https://m-home-i-game.com.cn/hot",
            tags=["热门", "推荐", "游戏"],
        ),
        KeywordNote(
            keyword="爱游戏 - 用户指南",
            description="帮助新用户快速了解平台功能、游戏规则和账户管理方法。",
            url="https://m-home-i-game.com.cn/guide",
            tags=["指南", "帮助", "入门"],
        ),
    ]


def filter_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    return [note for note in notes if tag in note.tags]


if __name__ == "__main__":
    notes = create_sample_notes()
    batch_print_notes(notes)
    export_notes_to_markdown(notes)
    print("已导出 keyword_notes.md")

    tag_to_filter = "游戏"
    filtered = filter_notes_by_tag(notes, tag_to_filter)
    print(f"\n包含标签 '{tag_to_filter}' 的笔记有 {len(filtered)} 条：")
    for note in filtered:
        print(f"  - {note.keyword}")