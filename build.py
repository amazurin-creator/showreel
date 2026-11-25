"""Собирает index.html. Запуск: python3 build.py"""
import html

e = html.escape


def fmt(n):
    return f'{n:,}'.replace(',', ' ')


# id, название, что это, инструменты, стоимость генерации
TOP = [
    ('lag-stewardess', 'AWIO · бортпроводница', 'Реклама приложения по авиационному английскому. Персонаж, сцена и голос сгенерированы.', 'ИИ-видео · голос · локализация'),
    ('cafe-w', 'Efaga · скетч в фитнес-кафе', 'Диалог двух персонажей, одни лица во всех сценах, POV-скан витрины.', 'Nano Banana · Kling · ElevenLabs · ≈ $3.5'),
    ('lag-pilot', 'AWIO · пилот', 'Кабина, техническая документация, крупные планы. Версии на ES, PT, TR.', 'ИИ-видео · голос · локализация'),
    ('mistake-m', 'Efaga · «#1 mistake»', '47% зрителей досматривают первые 3 секунды. Установка в 2,5 раза дешевле, чем со статики.', 'Flux · Kling · ElevenLabs · ≈ $3'),
    ('react', 'Efaga · реакция на вирусный рилс', 'Героиня с синхроном губ отвечает блогеру. 1,3 тыс. просмотров за сутки на аккаунте с 5 подписчиками.', 'Kling · lip-sync · ElevenLabs · ≈ $1.5'),
    ('lag-maritime', 'AWIO · моряк', '«Он знает, что делать, но не может сказать». Индустриальная сцена, эмоция крупным планом.', 'ИИ-видео · голос · локализация'),
]

LAG = [
    ('lag-it', 'IT-специалист', 'Офис, коллега через плечо, хук про технический английский.'),
    ('lag-mechanic', 'Авиатехник', 'Ангар, турбина, сигнальный жилет.'),
    ('lag-teacher', 'Учитель', 'Класс, доска с формулами.'),
    ('lag-online-teacher', 'Онлайн-преподаватель', 'Гарнитура, нервный урок по видеосвязи.'),
    ('lag-transport', 'Логистика', 'Склад, инструкции на английском.'),
    ('lag-duolingo', '«Как Duolingo, но для профи»', 'Финансовый английский, экран приложения в кадре.'),
    ('lag-notime', '«Нет времени учиться»', 'Утро с кофе, урок с телефона.'),
    ('lag-jp-notime', 'Япония · врач', '«10 минут в день». Японская версия для медицинского английского.'),
    ('lag-jp-doctor', 'Япония · палата', 'Разговор с пациентом-иностранцем.'),
]

EFAGA = [
    ('find-m', '«And now I find this?» — мужская', 'A/B-версия под мужскую аудиторию.', '≈ $0.7'),
    ('cafe-m', 'Скетч в кафе — мужская', 'Те же сцены с другим героем.', '≈ $3.5'),
    ('mistake-w', '«#1 mistake» — женская', 'CTR 3,2%, досмотр первых 3 секунд 46%.', '≈ $3'),
    ('find-w', '«And now I find this?»', 'Шок-хук за 3 секунды, потом три фичи приложения.', '≈ $0.7'),
    ('review-e05', 'Эфи разбирает рецепт', 'Серия: героиня в окошке смотрит чужой рецепт, приложение его считает.', '≈ $1.7'),
    ('review-e01', 'Эфи разбирает рецепт — эпизод 1', 'Полный формат с записью экрана.', '≈ $1.7'),
    ('one-tap', 'Моушн «one tap»', 'Маскоты, анимация в коде, два голоса.', '$0'),
    ('store-preview', 'Превью для App Store', 'Запись экрана в рамке телефона.', '$0'),
    ('whole-day', '«My whole day»', 'Органика на реальной еде.', '$0'),
    ('pizza-recipe', 'Рецепт пиццы', 'Органика с закадровым голосом.', '$0'),
    ('cheesecake', '«It fits»', 'Короткая органика.', '$0'),
    ('guess', '«Which one has more calories?»', 'Угадайка с отсчётом.', '$0'),
]

CHAR_TOP = [
    ('c-efi2-sheet', 'Лист персонажа: пять ракурсов одного человека. От него строятся все сцены', 'wide', '≈ $0.9 за весь лист'),
]
CHAR_SMALL = [
    ('c-efi2-face', 'Мастер-кадр лица', '≈ $0.04'),
    ('c-efi-kitchen', 'Кадр под синхрон губ', '≈ $0.06'),
    ('c-hero-shock-w', 'Герой хука', '≈ $0.06'),
    ('c-hero-shock-m', 'Мужская версия', '≈ $0.06'),
    ('c-mistake-w1', 'Примерочная', '≈ $0.06'),
    ('c-mistake-m1', 'Зал', '≈ $0.06'),
]
CHAR_MORE = [
    ('c-cafe-storyboard', 'Раскадровка: одни и те же лица в трёх сценах', 'wide', ''),
    ('c-mistake-storyboard', 'Раскадровка для двух аудиторий', 'wide', ''),
    ('c-efi1-sheet', 'Первая версия персонажа', 'wide', ''),
    ('c-stickers', '99 наклеек еды для интерфейса, ≈ $0.1 за штуку', 'wide', ''),
]

STATIC_TOP = ['s-goal', 's-duel', 's-plate', 's-onetap', 's-ban', 's-guess']
STATIC_MORE = ['s-split', 's-duo', 's-chat', 's-car1', 's-car2', 's-car3']
NATIVE = ['n-goal', 'n-guess', 'n-notes', 'n-pov', 'n-split', 'n-wieiad']
STORE = [f'st-frame-{i}' for i in range(1, 8)]

# код поста, просмотры, цена €, язык и ниша
IG = [
    ('DfQMmitMlbF', 138821, 150, 'PT-BR · авиация'),
    ('DfPYcqEo-Nv', 107815, 200, 'TR · медицина'),
    ('DeSF3hyMRhw', 83692, 300, 'ES · кардиология'),
    ('DdWT43WNS6-', 65682, 65, 'TR · медсестра'),
    ('De9xNg9tFNK', 42706, 300, 'PL · операционная'),
    ('DfjpVJUBe8r', 33146, 100, 'JP · студентка-медик'),
    ('DfIRMbWN5ZK', 30593, 130, 'FR · бортпроводница'),
    ('DepF-27sY1A', 21860, 90, 'DE · бортпроводник'),
    ('DelakpRhP97', 19302, 250, 'DE · пилот'),
]
REST = [
    ('DfjxKI3SBAv', 19448, 150, 'PT-BR'), ('DdfQgXItmYH', 18613, 150, 'ES'),
    ('DfStal9gpwn', 18321, 150, 'ES'), ('DezhdocBi8x', 17920, 300, 'DE'),
    ('DflF2IURa2F', 17841, 100, 'PT-BR'), ('DepIxk1OgKU', 14086, 100, 'FR'),
    ('DfH5shsONEi', 12849, 190, 'TR'), ('DfHsWukhlvz', 12591, 150, 'PT-BR'),
    ('DfpnuXxxUPR', 11887, 400, 'PL'), ('DfScvYHgAnc', 6669, 200, 'ES · NL'),
    ('DfXADvMq7q3', 6426, 100, 'PL'), ('DfkVs-oBaAE', 6425, 150, 'ES'),
    ('DfrnUIajJtF', 5572, 250, 'EN · KR'), ('DfO-E_NtBBv', 5563, 100, 'DE'),
    ('Df6t0PXzMwX', 3787, 200, 'EN'), ('Df9Ma_UC_wO', 977, 150, 'PL'),
]
ALL = IG + REST
VIEWS = sum(v for _, v, _, _ in ALL)
SPEND = sum(p for _, _, p, _ in ALL)
CPM = SPEND / VIEWS * 1000


def cpm(v, p):
    return f'€{p / v * 1000:.1f}'.replace('.', ',')


def vcard(i, t, n, g, big=False):
    cls = 'vcard big' if big else 'vcard'
    return (f'<figure class="{cls}"><button class="play" data-src="v/{i}.mp4" aria-label="Смотреть: {e(t)}">'
            f'<img src="v/{i}.jpg" alt="" loading="lazy"><span class="pbtn">▶</span></button>'
            f'<figcaption><b>{e(t)}</b><span>{e(n)}</span>{f"<em>{e(g)}</em>" if g else ""}</figcaption></figure>')


def more(label, inner):
    return f'<details class="more"><summary>{e(label)}</summary>{inner}</details>'


top = ''.join(vcard(*x, big=True) for x in TOP)
lag = ''.join(vcard(i, t, n, '') for i, t, n in LAG)
efaga = ''.join(vcard(i, t, n, g) for i, t, n, g in EFAGA)


def fig(i, t, cls, cost):
    c = f' <i>{e(cost)}</i>' if cost else ''
    return f'<figure class="{cls}"><img src="img/{i}.jpg" alt="{e(t)}" loading="lazy"><figcaption>{e(t)}{c}</figcaption></figure>'


chars = ''.join(fig(*x) for x in CHAR_TOP) + ''.join(fig(i, t, '', c) for i, t, c in CHAR_SMALL)
chars_more = ''.join(fig(*x) for x in CHAR_MORE)
imgs = lambda ids, alt: ''.join(f'<img src="img/{i}.jpg" alt="{alt}" loading="lazy">' for i in ids)
ig = ''.join(
    f'<figure class="ig"><div class="igwrap"><iframe src="https://www.instagram.com/p/{c}/embed/" loading="lazy" title="Рилс блогера" allowtransparency="true"></iframe></div>'
    f'<figcaption><b>{fmt(v)}</b> просмотров · €{p} · {cpm(v, p)} за 1000<br><span>{e(l)}</span></figcaption></figure>'
    for c, v, p, l in IG)
parts = [x + '</figure>' for x in ig.split('</figure>') if x]
ig_top, ig_more = ''.join(parts[:6]), ''.join(parts[6:])
rest = ''.join(
    f'<li><a href="https://www.instagram.com/p/{c}/" target="_blank" rel="noopener">{fmt(v)}<span>€{p} · {e(l)}</span></a></li>'
    for c, v, p, l in REST)

doc = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Артём Мазурин — ИИ-видео и креативы</title>
<meta name="description" content="ИИ-ролики, генерация персонажей, статика и инфлюенс-маркетинг под ключ.">
<meta property="og:title" content="Артём Мазурин — ИИ-видео и креативы"><meta property="og:image" content="img/c-efi2-sheet.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body>
<header class="hero"><div class="wrap">
<p class="kicker">Портфолио · 2025–2026</p>
<h1>Делаю рекламу<br>с&nbsp;<span>ИИ</span>: ролики, персонажи, статику</h1>
<p class="lead">Артём Мазурин. Сценарий, генерация героев и сцен, анимация, голос, монтаж. И блогеры под ключ: от первого сообщения до опубликованного рилса.</p>
<ul class="stats"><li><b>40+</b>ИИ-роликов, включая локализации</li><li><b>от $0,7</b>генерация одного ролика</li><li><b>{fmt(round(VIEWS / 1000))}&nbsp;тыс.</b>просмотров у рилсов блогеров</li><li><b>€{CPM:.1f}</b>за 1000 просмотров у блогеров</li></ul>
<nav><a href="#best">Лучшее</a><a href="#results">Результаты</a><a href="#lag">AWIO</a><a href="#efaga">Efaga</a><a href="#chars">Персонажи</a><a href="#static">Статика</a><a href="#influence">Блогеры</a></nav>
</div></header>
<main class="wrap">
<section id="best"><h2>Лучшее</h2><p class="sub">Шесть роликов, с которых стоит начать.</p><div class="vgrid top">{top}</div></section>

<section id="results"><h2>Как это отработало</h2><p class="sub">Цифры из рекламного кабинета Meta по креативам Efaga: Facebook и Instagram, iOS, США, Канада и Великобритания, оптимизация на установки.</p>
<ul class="res"><li><b>2,3%</b><span>CTR по ссылке в среднем по всем креативам</span><i>типичный CTR в Meta около 1%</i></li>
<li><b>47%</b><span>досматривают первые 3 секунды ролика «#1 mistake»</span><i>хорошим считается 25–30%</i></li>
<li><b>×2,5</b><span>дешевле установка с этого ролика, чем со статичного баннера</span><i>видео против статики в одной кампании</i></li>
<li><b>3%</b><span>CTR у баннера «Tap your goal weight» на 17 тыс. показов</span><i>статика, 4:5 и 9:16</i></li></ul>
<p class="note">Ноябрь 2026, Meta Ads Manager, 32 тыс. показов. Расход на рекламу не раскрываю.</p></section>

<section id="lag"><h2>AWIO · реклама для LAG</h2><p class="sub">2025, работал дизайнером креативов. Реклама приложения по профессиональному английскому: каждая профессия — свой персонаж и своя боль. Каждый ролик локализован на испанский, португальский и турецкий, часть — на японский.</p>
{more(f'Ещё {len(LAG)} роликов', f'<div class="vgrid">{lag}</div>')}</section>

<section id="efaga"><h2>Efaga · реклама счётчика калорий</h2><p class="sub">Платная реклама для Meta Ads и органика для Instagram. Полный цикл: сценарий, генерация кадров, анимация, голос, синхрон губ, монтаж. Под каждым роликом — сколько стоила генерация.</p>
{more(f'Ещё {len(EFAGA)} роликов', f'<div class="vgrid">{efaga}</div>')}</section>

<section id="chars"><h2>Генерация персонажей</h2><p class="sub">Главное в ИИ-видео — чтобы герой оставался одним человеком во всех кадрах. Сначала лист персонажа, потом от него каждая сцена.</p>
<div class="cgrid">{chars}</div>{more('Раскадровки и наклейки', f'<div class="cgrid">{chars_more}</div>')}</section>

<section id="static"><h2>Статика</h2><p class="sub">Баннеры для Meta Ads в форматах 4:5 и 9:16. Маскот, иллюстрации еды, реальные экраны приложения. Свёрстаны в коде, поэтому новая версия или язык стоят $0.</p>
<div class="sgrid">{imgs(STATIC_TOP, "Рекламный баннер")}</div>
{more('Ещё баннеры, нативные форматы и App Store', f'<div class="sgrid">{imgs(STATIC_MORE, "Рекламный баннер")}</div><h3>Нативные форматы</h3><div class="sgrid">{imgs(NATIVE, "Нативный баннер")}</div><h3>Страница в App Store</h3><div class="sgrid store">{imgs(STORE, "Скриншот App Store")}</div>')}</section>

<section id="influence"><h2>Блогеры под ключ</h2><p class="sub">Рилсы для EdTech-приложений по медицинскому и авиационному английскому. Весь цикл на мне: поиск и отбор авторов, первый контакт и вся переписка, переговоры о цене и правах, идея ролика под аудиторию блогера, план и бриф, сценарий, ревью черновиков, правки и монтаж, публикация в коллаборации, оплата и аналитика.</p>
<ul class="stats small"><li><b>{len(ALL)}</b>опубликованных рилсов</li><li><b>8</b>языков</li><li><b>€{fmt(SPEND)}</b>бюджет</li><li><b>{fmt(round(VIEWS / 1000))}&nbsp;тыс.</b>просмотров</li></ul>
<div class="iggrid">{ig_top}</div>
{more('Ещё интеграции', f'<div class="iggrid">{ig_more}</div><ul class="rest">{rest}</ul>')}</section>
</main>
<footer class="wrap"><p>Артём Мазурин</p></footer>
<dialog id="player"><button class="close" aria-label="Закрыть">✕</button><video controls playsinline></video></dialog>
<script>
const d=document.getElementById('player'),v=d.querySelector('video');
document.querySelectorAll('.play').forEach(b=>b.addEventListener('click',()=>{{v.src=b.dataset.src;d.showModal();v.play().catch(()=>{{}});}}));
const shut=()=>{{v.pause();v.removeAttribute('src');v.load();d.close();}};
d.querySelector('.close').onclick=shut;d.addEventListener('click',e=>{{if(e.target===d)shut();}});d.addEventListener('cancel',e=>{{e.preventDefault();shut();}});
</script></body></html>'''
open('index.html', 'w').write(doc)
print(f'views {VIEWS} spend {SPEND} cpm {CPM:.2f}')
