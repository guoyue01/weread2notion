# WeRead2Notion

将微信读书的书籍、划线和笔记同步到 Notion。

本项目使用微信读书 API Key 读取数据，并通过 GitHub Actions 定时同步到 Notion。新版不再需要复制微信读书 Cookie。

预览效果：https://malinkang.notion.site/weread2notion

> [!WARNING]
> WeRead2Notion 会在检测到书籍笔记更新时删除原来的同步页面，然后重新写入微信读书数据。请不要在同步生成的 Notion 书籍页面里添加自己的笔记、批注或其他重要内容，否则下次同步时可能会被删除且无法恢复。

## 使用文档

完整教程请查看：

https://www.notionhub.app/docs/weread2notion.html

文档里包含：

- Notion 模板复制和授权
- 微信读书 API Key 获取
- GitHub Fork 和 Actions 配置
- 常见问题排查

## 自动同步字段

同步开始时，程序会在 Notion 书籍数据库中自动创建并写入以下属性：

- 书籍详情：`字数`、`译者`。
- 阅读进度：`最后阅读时间`、`累计阅读时长`、`读完时间`、`是否已经开始阅读`。
- 笔记统计：`划线数`、`想法/点评数`、`书签数`。

现有模板的 `时间`、`阅读时长`属性仍然兼容。接口没有返回有效值时，对应属性会保持为空。
如果已有同名属性的类型不正确，程序会停止同步并提示修改或删除该属性。

已有书籍默认会被增量同步规则跳过。如需一次性补齐新增字段，请在 GitHub Actions 手动运行
`weread sync` 时勾选 `full_sync`。全量同步会删除并重建项目生成的书籍页面，完成后无需继续勾选。

## 关注公众号

如果你想获取后续更新，或了解更多 Notion 自动化工具，欢迎关注公众号：**Notion自动化**。

![公众号：Notion自动化](https://cdn.notionhub.app/notionhub/gzh.jpg)
