import streamlit as st

st.set_page_config(page_title="Từ Điển Emoji", page_icon="😊", layout="centered")
# CSS tùy chỉnh: nền đen, viền xanh
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    .main {
        border-top: 5px solid #00BFFF;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)


st.header("💬 TỪ ĐIỂN EMOJI", divider="blue")


eng = {
    "love": "❤️", "like": "👍", "hate": "💀", "funny": "😆", "sad": "😭",
    "angry": "😡", "bored": "🥱", "asleep": "😴", "excited": "🤩", "surprised": "😲",
    "cry": "😢", "pizza": "🍕", "burger": "🍔", "fries": "🍟", "coffee": "☕",
    "tea": "🫖", "cake": "🍰", "chocolate": "🍫", "icecream": "🍦",
    "cat": "🐱", "dog": "🐶", "monkey": "🙈", "panda": "🐼", "turtle": "🐢", "fish": "🐠",
    "me": "🙋", "you": "👉", "they": "👥", "friend": "🫶", "bro": "👊",
    "girl": "💁‍♀️", "boy": "🧑", "teacher": "👩‍🏫", "student": "🎓",
    "computer": "💻", "phone": "📱", "game": "🎮", "music": "🎶", "dance": "💃",
    "sleep": "🛌", "study": "📚", "money": "💸", "fire": "🔥", "party": "🎉",
    "wow": "🤯", "oops": "😅", "cool": "😎", "ok": "👌", "no": "🚫", "yes": "✅",
    "help": "🆘", "run": "🏃‍♂️", "lol": "😂", "bruh": "🤦‍♂️", "omg": "😱",
    "ghost": "👻", "sus": "🕵️"
}

viet = {
    "yêu": "❤️", "thích": "👍", "ghét": "💀", "buồn cười": "😆", "buồn": "😭",
    "tức giận": "😡", "chán": "🥱", "đang ngủ": "😴", "hào hứng": "🤩", "ngạc nhiên": "😲",
    "khóc": "😢", "pizza": "🍕", "burger": "🍔", "khoai tây chiên": "🍟", "cà phê": "☕",
    "trà": "🫖", "bánh": "🍰", "socola": "🍫", "kem": "🍦", "mèo": "🐱", "chó": "🐶",
    "khỉ": "🙈", "gấu trúc": "🐼", "rùa": "🐢", "cá": "🐠", "tôi": "🙋", "bạn": "👉",
    "họ": "👥", "bro": "👊", "giáo viên": "👩‍🏫", "học sinh": "🎓",
    "máy tính": "💻", "điện thoại": "📱", "game": "🎮", "nhạc": "🎶", "nhảy": "💃",
    "ngủ": "🛌", "học": "📚", "tiền": "💸", "cháy": "🔥", "party": "🎉",
    "wow": "🤯", "oops": "😅", "cool": "😎", "ok": "👌", "no": "🚫", "yes": "✅",
    "cứu": "🆘", "chạy": "🏃‍♂️", "lol": "😂", "bruh": "🤦‍♂️", "omg": "😱",
    "ma": "👻", "sus": "🕵️"
}


st.markdown("### Nhập câu của bạn vào đưây:")
col1, col2 = st.columns([3, 1])
with col1:
    sentence = st.text_input(" ", placeholder="Nhập câu có chứa cảm xúc ...")
with col2:
    lang = st.selectbox("Ngôn ngữ", ["Vietnamese", "English"])

# ====== Xử lý ======
def translate(sentence, lang):
    words = sentence.lower().split()
    if lang == "English":
        dictionary = eng
    else:
        dictionary = viet

    for i, word in enumerate(words):
        if word in dictionary:
            words[i] = dictionary[word]
    return " ".join(words)


if st.button("Chuyển đổi sang Emoji"):
    output = translate(sentence, lang)
    st.markdown(f"### ✅ Kết quả:")
    st.markdown(f"#### {output}")