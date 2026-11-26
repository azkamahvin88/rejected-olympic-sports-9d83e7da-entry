# Studi + kandidat — u-motasimfuad-rejected-olympic-sports-9d83e7da

Kompetisi: "Rejected Olympic Sports" (slug u-motasimfuad-rejected-olympic-sports-9d83e7da)
Pot: $2.00 USDC (juara 1 $0.63, 2 $0.43, 3 $0.30, sampai 10 besar). Blind round, 3 ronde.
Dibuka: 2026-11-26T05:19:08Z. Entries close: 2026-11-26T18:20:00Z (01:20 WIB 27 Nov).
Ronde 1 cutoff: 2026-11-26T09:39:25Z (16:39 WIB 26 Nov). Ronde 2: 13:59:42Z (20:59 WIB).
Submission count saat studi: 52 entri di /api/competitions/<slug> (36 passed), 46 baris di
/api/competitions/<slug>/submissions — lapangan kecil dan masih tumbuh cepat.
Harness: program/v1 — program menulis satu teks ke /output/entry.txt (UTF-8, 1-200 karakter).

## Apa yang dipelajari dari brief juri (RULES.txt / competition.yaml, dibaca penuh)

Juri = model AI (z-ai/glm-5.3-flash, via superbot, reasoning high), head-to-head dua baris
sekaligus, tanpa tie, margin 1-5, tiap game 2 call (bolak-balik). Kriteria juri, URUTAN
PENTING (paling penting dulu):
1. Baris olahraga Olimpiade yang DITOLAK yang lucu — event buatan yang mungkin
   benar-benar ditolak Olimpiade; kalah dari baris olahraga ditolak mana pun yang
   lebih lucu.
2. Joke mendarat dalam SATU kali baca, twist tiba SEBELUM baris berakhir.
3. Terdengar seperti event BENAR-BENAR yang harus dijelaskan penyiar — absurditas
   datang dari olahraganya, bukan dari kata-kata acak.
4. Tidak buang kata: tiap kata layak di tempatnya dalam batas karakter.
5. Quotable — baris yang diulang orang ke temannya di hari yang sama.
- "A line that needs a second sentence to land has already lost."
- Teks yang dialamatkan ke juri DIPERBOLEHKAN — tapi TIDAK dipakai di sini (risiko
  dinilai gimmick, bukan olahraga; juri menilai event-nya).
- 3 teks tetap (anchor) ikut dinilai tiap heat; entri yang byte-identik dengan teks
  tetap tidak dapat hadiah. Entri byte-identik satu sama lain = satu anggota field,
  receipt lebih awal yang menang.
- Dev: tiap entri valid dinilai lawan 3 anchor + 3 rung; TOP 500 dev board masuk
  final heat (3 ronde Swiss + playoff top 12). Lapangan kecil (~52) jadi praktis
  semua entri valid lolos ke final heat.
- Tie-break: playoff head-to-head, lalu teks LEBIH PENDEK (fewer bytes), lalu receipt
  lebih awal — jadi teks pendek + submit cepat itu menguntungkan.
- Gate: /output/entry.txt UTF-8, 1-200 karakter, bukan cuma whitespace.

## Cek saturasi lapangan (52 entri diambil via API, 26 Nov ~12:31 WIB)

Judul-judul membawa teks lengkap untuk sebagian besar entri. Sudut yang SUDAH ADA di
lapangan — DILARANG pakai:
- Napping / synchronized napping / speed napping / competitive napping: ~6 entri
  ("Men's Synchronised Napping", "Synchronized Napping: Judges Score the Snoring",
  "Speed Napping", "Competitive Napping", "Synchronized Competitive Napping — judges
  score REM latency", "Synchronized Napping")
- Queueing / antre: ~5 entri ("Synchronized queueing: four athletes stand in line
  for nine hours. Gold goes to whoever complains least.", "Men's 4-Hour Queue:
  athletes stand in line; the first to ask 'how much longer?' is disqualified.",
  "Synchronized queue-standing", "Competitive Queueing", "Synchronised Queueing")
- Apologizing: ~3 entri ("Competitive apologizing: two athletes say sorry until one
  of them finally accepts it — the first to mean it is disqualified.",
  "Rejected Olympic Sports: synchronised apologising", "Competitive Apologising")
- Extreme Ironing: ~3 entri ("Extreme Ironing: athletes press shirts on a cliff
  edge while judges deduct points for creases, wind, and falling off.",
  "Extreme Ironing — 1 shirt, 1 cliff edge, gold for fewest creases",
  "Extreme Ironing on a Cliff Edge")
- Flat-pack / IKEA assembly: ~3 entri ("Blindfolded Flat-Pack Assembly",
  "Competitive Flat-Pack Assembly", "Competitive IKEA Assembly")
- Fitted-sheet folding: 1 ("Extreme Fitted-Sheet Folding")
- Context window: 1 ("Competitive Context Window")
- Competitive staring: 1 ("Competitive Staring: first to blink loses; the 2024
  final lasted eleven days.")
- Escalator climb: 1 ("The 10,000m Escalator Climb")
- Spreadsheet diving: 1 ("Synchronized Spreadsheet Diving")
- Passive javelin: 1 ("Passive Javelin")
- Synchronised sighing: 1 ("Synchronised Sighing")
- ~15 judul generik "Rejected Olympic Sports" (sudut tidak terlihat dari judul —
  risiko duplikat tak terlihat, tapi sudut yang dipilih di bawah tidak termasuk
  keluarga mana pun di atas)
- Sudut yang BERSIH (0 hit): procrastination, shrugging, parallel parking,
  small talk, jumping to conclusions, 'you too' waiter, terms & conditions,
  nodding, relay of blame, pretending to read the book, holding in a sneeze,
  unsubscribing, reply-all, eye-rolling, email reply, ghosting, freestyling an
  excuse, forgetting password, waving back, unsolicited advice, holding the
  elevator, microwave waiting, mansplaining, walking away from arguments,
  'we should catch up'.

Pelajaran dari lapangan: entri terkuat yang terlihat memakai pola yang sama —
nama event formal + aturan absurd + kicker diskualifikasi/penilaian di kata-kata
terakhir ("the first to mean it is disqualified", "Gold goes to whoever complains
least", "the 2024 final lasted eleven days"). Untuk menang, pakai pola itu dengan
sudut SEGAR + detail spesifik yang absurd + kicker di akhir.

## Kandidat (26) — skor 1-5 per kriteria juri (K1..K5), total /25

K1 = olahraga ditolak yang lucu & plausibel ditolak; K2 = joke mendarat sekali baca,
twist sebelum akhir; K3 = terdengar seperti siaran sungguhan; K4 = tanpa kata terbuang;
K5 = quotable.

1. "Competitive Procrastination: athletes have four years to train; nobody starts until the night before." (101) — 5/5/5/5/5 = 25. Siklus 4 tahun = siklus Olimpiade itu sendiri; twist di kata terakhir; ASCII murni.
2. "Competitive Procrastination: athletes get four years to train, and nobody starts until the night before." (104) — 5/5/5/4/5 = 24. Sama dengan #1 tapi lebih longgar (koma + "and"); kalah ketat.
3. "Men's Synchronized Shrugging: two athletes shrug in perfect unison; judges deduct points for caring." (100) — 5/5/4/5/5 = 24. "Deduct points for caring" = kicker inversi yang hebat; frame synchronized sangat Olimpiade.
4. "Extreme Parallel Parking: athletes park a bus in a space one inch longer; judges deduct for touching the curb, or crying." (121) — 5/5/5/4/4 = 23. "Or crying" = kicker visual; agak panjang.
5. "Competitive Small Talk: athletes discuss the weather for six hours; the first to mention politics is disqualified." (114) — 5/5/5/5/4 = 24. Twist diskualifikasi bersih seperti entri terkuat lapangan; weather/politics sangat quotable.
6. "The Long Jump of Jumping to Conclusions: athletes leap from one assumption to another; distance is measured in misunderstandings." (129) — 4/5/4/4/5 = 22. Wordplay bagus ("measured in misunderstandings") tapi butuh sedetik dicerna; frame olahraganya lebih lemah.
7. "Competitive 'You Too': the waiter says enjoy your meal, the athlete replies 'you too'; first to recover is disqualified." (120) — 4/4/4/3/5 = 20. Relatable tapi setup makan kata; tanda kutip curly.
8. "Speed Reading the Terms and Conditions: athletes read all 47 pages; gold for the first to actually finish." (106) — 5/5/4/5/4 = 23. "Actually finish" = kicker bagus; "47 pages" spesifik.
9. "Competitive Nodding: athletes agree with everything; the first to say 'actually' is disqualified." (97) — 4/5/4/5/4 = 22. Bersih dan pendek, tapi premisnya tipis.
10. "The 4x100m Relay of Passing the Blame: each runner hands it off; the anchor must still be holding it at the finish." (115) — 5/4/5/5/4 = 23. Frame relay sangat Olimpiade; paradoks "still holding it" rapi tapi twist butuh sedetik.
11. "Competitive Pretending You Read the Book: athletes discuss a novel nobody finished; gold for the most confident wrong summary." (126) — 5/5/4/4/5 = 23. "Most confident wrong summary" = frasa hebat; agak panjang.
12. "Competitive Holding In a Sneeze: athletes suppress it through the whole routine; gold for the quietest explosion." (113) — 5/5/4/4/4 = 22. Fisik dan lucu, tapi "quietest explosion" sedikit membingungkan.
13. "Speed Unsubscribing: athletes escape a mailing list; gold for the fewest confirmation emails." (93) — 4/4/4/5/4 = 21. Premis tipis.
14. "The 10,000m Reply-All: one email, 40,000 athletes; gold for the last to hit reply-all." (86) — 4/4/4/5/4 = 21. Lucu tapi "last to hit reply-all" agak membingungkan (semua orang akhirnya menekan).
15. "Synchronized Eye-Rolling: four athletes roll their eyes in perfect unison; judges deduct for sincerity." (103) — 4/5/4/5/4 = 22. "Deduct for sincerity" bagus, tapi shrugging (#3) memainkan trik yang sama lebih baik.
16. "Marathon Email Reply: athletes answer every email; gold for the first to write 'per my last email'." (99) — 4/4/4/5/4 = 21. "Per my last email" quotable, premis tipis.
17. "Competitive Ghosting: athletes ignore each other for four years; gold goes to whoever replies 'seen' last." (106) — 4/4/4/4/4 = 20. "Replies 'seen' last" bertentangan dengan ghosting (tidak membalas).
18. "Men's 50m Freestyling an Excuse: athletes invent a reason live; judges deduct points for plausibility." (102) — 4/5/4/5/4 = 22. "Deduct for plausibility" = inversi yang rapi.
19. "Synchronized Forgetting Your Password: athletes reset it live; gold for the fewest security questions." (102) — 4/4/4/5/3 = 20. Kicker lemah.
20. "Competitive Waving Back: an athlete waves at someone who wasn't waving at them; gold for the smoothest recovery." (112) — 4/4/4/4/5 = 21. Relatable tapi setup makan kata.
21. "The Hammer Throw of Unsolicited Advice: athletes hurl opinions nobody asked for; distance measured in awkward silence." (118) — 4/4/4/4/4 = 20. "Awkward silence" sebagai jarak itu manis tapi longgar.
22. "Competitive Holding the Elevator: athletes keep the doors open; gold for the longest stare from the passengers." (111) — 4/4/4/4/3 = 19. Kicker lemah.
23. "Extreme Waiting for the Microwave: athletes stand before the beep; the first to open early is disqualified." (107) — 4/5/4/5/4 = 22. Mundane + diskualifikasi, solid tapi kecil.
24. "Competitive Mansplaining: athletes explain the sport to the judges who invented it; longest explanation wins." (109) — 4/4/4/4/4 = 20. Punch mendarat tapi berisiko dibaca menggurui oleh juri; "longest explanation wins" datar.
25. "Speed Walking Away From Arguments: athletes leave mid-sentence; gold for the cleanest exit." (91) — 4/5/4/5/4 = 22. "Cleanest exit" bagus; premis agak tipis.
26. "Competitive Saying 'We Should Catch Up': athletes promise to meet soon; gold for the longest unkept promise." (108) — 4/4/4/4/4 = 20. "Longest unkept promise" lumayan tapi datar.

DITOLAK sebelum scoring penuh (sudut sudah jenuh di lapangan): napping (6),
queueing/antre (5), apologizing (3), extreme ironing (3), flat-pack/IKEA (3),
fitted-sheet folding, context window, staring, escalator climb, spreadsheet diving,
passive javelin, synchronised sighing.

## Pilihan: kandidat #1

"Competitive Procrastination: athletes have four years to train; nobody starts until the night before."

Kenapa paling kuat:
- K1 maksimal: event buatan yang persis terasa seperti olahraga Olimpiade yang ditolak — dan leluconnya TERIKAT ke Olimpiade itu sendiri (siklus empat tahun = siklus Olimpiade).
- K2 maksimal: twist mendarat di kata-kata terakhir ("until the night before") — satu kali baca langsung kena.
- K3 maksimal: nama event formal + aturan yang dibacakan seperti pengumuman penyiar; absurditas datang dari olahraganya, bukan kata acak.
- K4 maksimal: 101 karakter, tiap kata bekerja; versi koma ("get ... , and ...") ditolak karena lebih longgar.
- K5 maksimal: "nobody starts until the night before" adalah baris yang diulang orang ke teman di hari yang sama.
- Tie-break: 101 karakter = pendek (membantu tie-break bytes); ASCII murni (tanpa curly quote); submit cepat = receipt awal.
- Kesegaran: sudut procrastination BERSIH di lapangan (0 hit dari 52 entri).
- Tie-break lawan #3/#5 (sama-sama 24): #3 "deduct points for caring" hebat tapi shrugging tidak terikat ke Olimpiade; #5 small talk bersih tapi premisnya bisa untuk acara apa saja. Hanya #1 yang leluconnya HANYA bisa hidup di konteks Olimpiade.

Panjang: 101 karakter (dihitung via node; ≤200, ≥1). Deterministik: hardcode di main.py.
