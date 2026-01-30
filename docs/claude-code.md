# Claude Code 入門ガイド

Claude Codeは、Anthropicが提供する公式CLIツール。ターミナルから直接Claudeを使って開発ができる。

## Claude Code とは

従来のChatGPTやClaude Webとの違い：

| 特徴 | Web版 Claude | Claude Code |
|------|-------------|-------------|
| 操作場所 | ブラウザ | ターミナル |
| ファイル操作 | 手動コピペ | 直接読み書き可能 |
| コマンド実行 | 不可 | 可能（git, npm等） |
| プロジェクト理解 | 限定的 | フォルダ全体を把握 |

開発者にとっての最大のメリットは、**プロジェクトのコンテキストを維持したまま**作業できること。

---

## インストール

### 必要条件

- Node.js 18以上
- npm または yarn

### インストールコマンド

```bash
npm install -g @anthropic-ai/claude-code
```

### 初回セットアップ

```bash
claude
```

初回起動時にブラウザが開き、Anthropicアカウントでログインする。

---

## 基本的な使い方

### 起動

プロジェクトのルートディレクトリで：

```bash
claude
```

### 基本コマンド

| コマンド | 説明 |
|----------|------|
| `/help` | ヘルプを表示 |
| `/clear` | 会話履歴をクリア |
| `/compact` | 会話を要約して圧縮 |
| `/cost` | 現在のセッションのコストを表示 |

### 使用例

```bash
# プロジェクトを開いて起動
cd my-project
claude

# 質問する
> このプロジェクトの構造を説明して

# ファイルを修正してもらう
> src/utils.py のエラーハンドリングを改善して

# テストを実行
> pytest を実行して結果を教えて
```

---

## Claude Skill とは

Claude Skillは、よく使う指示をテンプレート化して再利用できる機能。

### Skillの場所

```
~/.claude/skills/
├── your-skill-name/
│   └── SKILL.md
└── another-skill/
    └── SKILL.md
```

### Skillの呼び出し方

```bash
# ターミナルで
claude /skill-name

# または会話中に
> /skill-name
```

---

## Skill の作成方法

### Step 1: ディレクトリ作成

```bash
mkdir -p ~/.claude/skills/my-skill
```

### Step 2: SKILL.md を作成

```bash
touch ~/.claude/skills/my-skill/SKILL.md
```

### Step 3: プロンプトを記述

```markdown
# My Custom Skill

このスキルの説明をここに書く。

## 実行内容

1. まず〇〇を確認する
2. 次に△△を実行する
3. 最後に□□を出力する
```

---

## Skill 実践例

### 例1: dev-init（プロジェクト初期化）

```markdown
# Dev Init Skill

新規プロジェクトの初期化を行う。

## 実行内容

1. プロジェクト構造を作成
   - src/
   - tests/
   - docs/

2. 必要なファイルを生成
   - README.md
   - .gitignore
   - 設定ファイル

3. DEVLOG.md を初期化
```

### 例2: vibe-coding（開発アシスタント）

```markdown
# Vibe Coding Skill

開発タスクをサポートするスキル。

## 対応内容

- コード修正リクエスト
- 機能実装
- デバッグ支援
- アーキテクチャ相談

## ルール

- AGENTS.md のルールに従う
- 変更前に必ず提案を行う
- 日本語で応答する
```

---

## AGENTS.md との組み合わせ

Claude CodeとAGENTS.mdを組み合わせることで、より効果的な開発が可能になる。

### ワークフロー

```
1. プロジェクトに AGENTS.md を配置
   └── AIの動作ルールを定義

2. Claude Code を起動
   └── claude コマンドで開始

3. 開発を進める
   └── AIは AGENTS.md のルールに従って動作

4. 必要に応じて Skill を活用
   └── /skill-name で呼び出し
```

### ベストプラクティス

- **AGENTS.md**: プロジェクト全体のルール（全員が従うべき指針）
- **Skill**: 個人の作業効率化（よく使う操作のショートカット）

両方を使い分けることで、一貫性のある開発と個人の生産性向上を両立できる。

---

## トラブルシューティング

### よくある問題

| 問題 | 解決策 |
|------|--------|
| コマンドが見つからない | `npm install -g @anthropic-ai/claude-code` を再実行 |
| ログインできない | ブラウザのCookieをクリアして再試行 |
| ファイルが読めない | プロジェクトルートで `claude` を起動しているか確認 |
| Skillが認識されない | `~/.claude/skills/` のパスとファイル名を確認 |

### サポート

- 公式ドキュメント: https://docs.anthropic.com/claude-code
- GitHub Issues: https://github.com/anthropics/claude-code/issues
