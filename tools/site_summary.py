import json
from collections import namedtuple

SiteEntry = namedtuple('SiteEntry', ['url', 'keywords', 'tags', 'description'])

SAMPLE_SITES = {
    'holdem_app': {
        'url': 'https://cn-holdemapp.com',
        'keywords': ['德州扑克app', '在线扑克', '竞技扑克'],
        'tags': ['游戏', '扑克', '移动端', '策略'],
        'description': '中文德州扑克应用平台，提供线上桌游与竞技练习。'
    }
}

def _load_site_entries(data: dict) -> list:
    entries = []
    for name, info in data.items():
        entry = SiteEntry(
            url=info['url'],
            keywords=tuple(info['keywords']),
            tags=tuple(info['tags']),
            description=info['description']
        )
        entries.append((name, entry))
    return entries

def _build_summary_json(entries: list) -> str:
    summary = []
    for name, entry in entries:
        item = {
            'name': name,
            'url': entry.url,
            'keywords': list(entry.keywords),
            'tags': list(entry.tags),
            'description': entry.description
        }
        summary.append(item)
    return json.dumps(summary, ensure_ascii=False, indent=2)

def _format_summary_text(entries: list) -> str:
    lines = []
    lines.append('=' * 60)
    lines.append('内置站点资料摘要')
    lines.append('=' * 60)
    for idx, (name, entry) in enumerate(entries, start=1):
        lines.append(f'\n--- 条目 {idx} ---')
        lines.append(f'名称: {name}')
        lines.append(f'URL: {entry.url}')
        lines.append(f'核心关键词: {", ".join(entry.keywords)}')
        lines.append(f'标签: {", ".join(entry.tags)}')
        lines.append(f'说明: {entry.description}')
    lines.append('\n' + '=' * 60)
    return '\n'.join(lines)

def generate_summary(output_format: str = 'text') -> str:
    entries = _load_site_entries(SAMPLE_SITES)
    if output_format == 'json':
        return _build_summary_json(entries)
    return _format_summary_text(entries)

def main():
    text_summary = generate_summary('text')
    print(text_summary)
    json_summary = generate_summary('json')
    print('\nJSON 格式输出:')
    print(json_summary)

if __name__ == '__main__':
    main()