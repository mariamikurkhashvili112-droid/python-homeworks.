# ფილმების Flask + MongoDB პროექტი — ინსტრუქცია

## პროექტის სტრუქტურა (MVC)

```
movie_flask_app/
├── app/
│   ├── models/
│   │   └── movie_model.py      → Model (ბაზასთან კომუნიკაცია)
│   ├── controllers/
│   │   └── movie_controller.py → Controller (ლოგიკა/routes)
│   ├── templates/
│   │   └── index.html          → View (გვერდი)
│   ├── static/
│   │   └── style.css
│   └── __init__.py
├── config.py
├── run.py
├── seed_db.py
└── requirements.txt
```

## 1. MongoDB-ს დაყენება

**მნიშვნელოვანი:** pgAdmin4 გამოიყენება PostgreSQL-თან სამუშაოდ, MongoDB კი
სულ სხვა ტიპის ბაზაა (NoSQL). pgAdmin4 ამ დავალებისთვის არ გამოგადგებათ.

MongoDB-სთვის დაგჭირდებათ:
1. **MongoDB Community Server** — თავად ბაზის სერვერი.
   ჩამოტვირთეთ აქედან: https://www.mongodb.com/try/download/community
   (Mac-ისთვის აირჩიეთ macOS ვერსია).
2. **MongoDB Compass** (არასავალდებულო, მაგრამ ძალიან სასარგებლო) — ეს არის
   pgAdmin4-ის ანალოგი, უბრალოდ MongoDB-სთვის. მასში ვიზუალურად ნახავთ
   თქვენს კოლექციებსა და დოკუმენტებს.
   ჩამოტვირთვა: https://www.mongodb.com/try/download/compass

დაყენების შემდეგ დარწმუნდით, რომ MongoDB სერვერი გაშვებულია
(ტერმინალში `mongod` ან უბრალოდ დააინსტალირეთ Homebrew-ით):

```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

## 2. პროექტის გახსნა PyCharm-ში

1. PyCharm-ში: `File → Open` და აირჩიეთ `movie_flask_app` ფოლდერი.
2. შექმენით ვირტუალური გარემო (თუ PyCharm თავად არ შემოგთავაზებთ):
   `File → Settings → Project → Python Interpreter → Add Interpreter → Venv`.
3. გახსენით ტერმინალი PyCharm-ში (ქვედა ზოლში `Terminal`) და დააინსტალირეთ
   საჭირო ბიბლიოთეკები:

```bash
pip install -r requirements.txt
```

## 3. ფილმების ბაზაში შეყვანა

გაუშვით `seed_db.py` **ერთხელ** — ის შეავსებს MongoDB-ს მოცემული ფილმებით:

```bash
python seed_db.py
```

თუ გინდათ ვიზუალურად შეამოწმოთ, გახსენით MongoDB Compass, დაუკავშირდით
`mongodb://localhost:27017/`-ს და ნახავთ `movies_db` ბაზაში `movies`
კოლექციას.

## 4. Flask აპლიკაციის გაშვება

```bash
python run.py
```

ტერმინალში დაინახავთ რაღაც ასეთს:
`Running on http://127.0.0.1:5000`

გახსენით ბრაუზერში: **http://127.0.0.1:5000**

## რას ხედავთ გვერდზე

- ცხრილს ყველა ფილმით (დასახელება, წელი, რეიტინგი, ჟანრი, ხანგრძლივობა).
- ტექსტის ფერი იცვლება რეიტინგის მიხედვით (მწვანე ≥ 9, ნარინჯისფერი
  8.5–8.99, ნაცრისფერი დანარჩენი) — ეს კეთდება `index.html`-ში Jinja-ს
  `{% if %}` პირობებით.
- ფილმების საერთო რაოდენობა და საშუალო ხანგრძლივობა — ორივე
  გამოთვლილია დინამიურად `movie_model.py`-ში (Python-ის კოდით,
  ხელით არაფერია დათვლილი).

## როგორ მუშაობს MVC აქ

- **Model** (`movie_model.py`) — მხოლოდ ეს ფაილი ესაუბრება ბაზას.
- **Controller** (`movie_controller.py`) — იძახებს Model-ს, ამზადებს
  მონაცემებს და უგზავნის View-ს.
- **View** (`index.html`) — მხოლოდ აჩვენებს მონაცემებს, ლოგიკას არ შეიცავს.

## თუ რამე არ მუშაობს

- `pymongo.errors.ServerSelectionTimeoutError` → MongoDB სერვერი არ არის
  გაშვებული (`brew services start mongodb-community`).
- ცარიელი ცხრილი → არ გაუშვიათ `seed_db.py`, ან ბაზის სახელი/კოლექცია
  არასწორია `config.py`-ში.
