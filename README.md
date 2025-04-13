# 🎵 Hudobný odporúčací systém založený na hlbokých neurónových sieťach
**Autor:** Sebastian Hresko  
**Diplomová práca – 2025**

Tento projekt sa zaoberá vývojom inteligentného hudobného odporúčacieho systému, ktorý využíva hlboké neurónové siete a audio embeddingy na odporúčanie podobných skladieb na základe ich zvukových vlastností.

---

## 📁 Dataset

Použitý dataset:  
[🎼 Songs Dataset (Kaggle)](https://www.kaggle.com/datasets/jashanjeetsinghhh/songs-dataset)

Dataset obsahuje základné informácie o skladbách, vrátane:
- Názov skladby
- Interpret
- Žáner
- Trvanie
- Zvukové a štatistické parametre
- `preview_url` – URL odkaz na 30-sekundový audio záznam skladby

> 🧾 **Poznámka:** Dataset vo formáte `.csv` sa nachádza v priečinku `datasets/`.

---

## 🎧 Sťahovanie MP3 ukážok

Na sťahovanie 30-sekundových MP3 ukážok využívame Python skript `mp3_downloader.py`, ktorý:
- Načíta dataset z priečinka `datasets/`
- Vytiahne atribút `preview_url`
- Stiahne a uloží MP3 ukážky do lokálneho priečinka

---

## 🎙️ Audio embedovacie modely

Na extrakciu vektorových reprezentácií zvuku používame niekoľko pokročilých modelov:

### 🔹 [OpenL3](https://openl3.readthedocs.io/en/latest/installation.html)
- Trénovaný na kombinovaných zvukovo-vizuálnych dátach
- Vhodný pre generalizované audio embeddingy

### 🔹 [Wav2Vec 2.0 (Facebook)](https://huggingface.co/facebook/wav2vec2-base)
- Výkonný model pre spracovanie zvuku a reči
- Založený na transformer architektúre

### 🔹 [PANNs (Pretrained Audio Neural Networks)](https://github.com/qiuqiangkong/panns_inference)
- Univerzálne modely pre zvukové úlohy ako klasifikácia a rozpoznávanie

### 🔹 [VGGish](https://github.com/tensorflow/models/blob/master/research/audioset/vggish/README.md)
- Audio embedding model trénovaný na YouTube-8M datasete
- Vhodný na extrakciu všeobecných zvukových príznakov

---

## 🧠 Vektorová databáza: Qdrant

Na ukladanie a vyhľadávanie podobných skladieb používame:

### 🔸 [Qdrant](https://qdrant.tech/documentation/quick_start/)
- Vysokovýkonná vektorová databáza optimalizovaná pre podobnostné vyhľadávanie
- Podpora REST API a klientov v rôznych jazykoch (Python, JS, atď.)
- Umožňuje škálovateľné a rýchle porovnávanie embedovaných reprezentácií

