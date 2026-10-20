import streamlit as st
import pickle

from auth import register_user, login_user
from history import save_detection, get_history


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="🛡️",
    layout="wide"
)



# =========================================================
# CYBER SECURITY NAVY + PURPLE THEME
# ONLY DESIGN — NO STRUCTURE CHANGES
# =========================================================

st.markdown("""
<style>

/* MAIN WEBSITE */
.stApp {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(91, 55, 190, 0.28),
            transparent 25%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(37, 62, 145, 0.20),
            transparent 28%
        ),
        #080b2b !important;

    color: #ffffff !important;
}


/* MAIN CONTENT */
.block-container {
    max-width: 1200px !important;
}


/* HEADINGS */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}


/* NORMAL TEXT */
p, label {
    color: #c6c5d8 !important;
}


/* SIDEBAR */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #171743,
            #11132f
        ) !important;

    border-right: 1px solid #29275c !important;
}


/* SIDEBAR TEXT */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #b8b7ce !important;
}


/* SIDEBAR MENU HOVER */
div[role="radiogroup"] label:hover {
    background: #28245d !important;
    border-radius: 8px !important;
}


/* BUTTONS */
.stButton > button {
    background:
        linear-gradient(
            135deg,
            #6745f5,
            #9b3fe5
        ) !important;

    color: #ffffff !important;

    border: 1px solid #8068ff !important;

    border-radius: 8px !important;

    font-weight: 700 !important;

    transition: 0.2s ease;
}


/* BUTTON HOVER */
.stButton > button:hover {
    background:
        linear-gradient(
            135deg,
            #795aff,
            #ae4df0
        ) !important;

    border-color: #b49cff !important;

    box-shadow:
        0 0 20px rgba(119, 82, 255, 0.35) !important;
}


/* TEXT INPUT */
.stTextInput input {
    background: #151638 !important;

    color: #ffffff !important;

    border: 1px solid #38356c !important;

    border-radius: 8px !important;
}


/* TEXT AREA */
.stTextArea textarea {
    background: #151638 !important;

    color: #ffffff !important;

    border: 1px solid #38356c !important;

    border-radius: 8px !important;
}


/* INPUT FOCUS */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #805cff !important;

    box-shadow:
        0 0 0 1px #805cff !important;
}


/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background: #141637 !important;

    border: 1px solid #2e2b5d !important;

    border-radius: 9px !important;

    padding: 5px !important;
}


/* TAB TEXT */
.stTabs [data-baseweb="tab"] {
    color: #9492ad !important;
}


/* ACTIVE TAB */
.stTabs [aria-selected="true"] {
    background:
        linear-gradient(
            135deg,
            #6745f5,
            #9145df
        ) !important;

    color: #ffffff !important;

    border-radius: 7px !important;
}


/* METRIC CARDS */
div[data-testid="stMetric"] {
    background:
        linear-gradient(
            135deg,
            #282061,
            #3b267b
        ) !important;

    border: 1px solid #514594 !important;

    border-radius: 13px !important;

    padding: 16px !important;
}


/* METRIC LABEL */
div[data-testid="stMetricLabel"] {
    color: #c2c0dc !important;
}


/* METRIC NUMBER */
div[data-testid="stMetricValue"] {
    color: #ffffff !important;

    font-weight: 800 !important;
}


/* BORDER CONTAINERS */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #141638 !important;

    border: 1px solid #2d2a5c !important;

    border-radius: 12px !important;
}


/* DIVIDERS */
hr {
    border-color: #292752 !important;
}


/* SUCCESS */
div[data-testid="stAlert"] {
    border-radius: 9px !important;
}


/* SCROLLBAR */
::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #080b2b;
}

::-webkit-scrollbar-thumb {
    background: #403b73;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #765cff;
}

</style>
""", unsafe_allow_html=True)
# =========================================================
# DASHBOARD PROFESSIONAL CYBER SECURITY STYLING
# DESIGN ONLY - NO STRUCTURE CHANGES
# =========================================================

st.markdown("""
<style>

/* =====================================================
   DASHBOARD TITLE
   ===================================================== */

.dashboard-title {
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
}

.dashboard-subtitle {
    color: #8585a5;
    font-size: 14px;
}


/* =====================================================
   METRIC CARDS
   ===================================================== */

div[data-testid="stMetric"] {
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #211b55 0%,
            #33216d 55%,
            #45217c 100%
        ) !important;

    border: 1px solid #55458f !important;

    border-radius: 14px !important;

    padding: 20px !important;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.20) !important;

    transition: 0.25s ease;
}


/* CARD HOVER */

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);

    border-color: #8c6cff !important;

    box-shadow:
        0 10px 30px rgba(101, 70, 230, 0.25) !important;
}


/* METRIC LABEL */

div[data-testid="stMetricLabel"] {
    color: #c1bddb !important;

    font-size: 13px !important;

    font-weight: 600 !important;
}


/* METRIC NUMBER */

div[data-testid="stMetricValue"] {
    color: #ffffff !important;

    font-size: 30px !important;

    font-weight: 800 !important;
}


/* =====================================================
   DASHBOARD CONTENT CARDS
   ===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        linear-gradient(
            145deg,
            #151638,
            #1b1a45
        ) !important;

    border: 1px solid #302d63 !important;

    border-radius: 14px !important;

    box-shadow:
        0 7px 20px rgba(0, 0, 0, 0.18) !important;
}


/* =====================================================
   RECENT DETECTION CARDS
   ===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"]:hover {

    border-color: #51459a !important;

    box-shadow:
        0 8px 25px rgba(83, 62, 180, 0.18) !important;
}


/* =====================================================
   SECTION HEADINGS
   ===================================================== */

.stMarkdown h2,
.stMarkdown h3 {
    color: #ffffff !important;
}


/* =====================================================
   SECURITY NOTE
   ===================================================== */

.stAlert {
    background: #151638 !important;

    border: 1px solid #39356e !important;

    border-radius: 10px !important;

    color: #d0cde3 !important;
}


/* =====================================================
   SIDEBAR ACTIVE FEEL
   ===================================================== */

section[data-testid="stSidebar"] {
    box-shadow:
        8px 0 30px rgba(0, 0, 0, 0.15);
}


/* =====================================================
   LOGOUT BUTTON
   ===================================================== */

section[data-testid="stSidebar"] .stButton > button {
    background: #1b193d !important;

    border: 1px solid #393565 !important;

    color: #bdbbd2 !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #2b2457 !important;

    border-color: #745cff !important;

    color: #ffffff !important;
}


/* =====================================================
   DETECTION RESULT TEXT
   ===================================================== */

.stSuccess {
    border-color: #3d8c70 !important;
}

.stError {
    border-color: #9b3d67 !important;
}

.stWarning {
    border-color: #92713a !important;
}


/* =====================================================
   CLEAN SCROLLBAR
   ===================================================== */

::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-track {
    background: #090b25;
}

::-webkit-scrollbar-thumb {
    background: #3d376c;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #765cff;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "entered_system" not in st.session_state:
    st.session_state["entered_system"] = False


# =========================================================
# PAGE 1 - WELCOME PAGE
# =========================================================
# =========================================================
# PAGE 1 - WELCOME / LANDING PAGE
# =========================================================

if not st.session_state["entered_system"]:

    # Page background
    st.markdown("""
    <style>

    .block-container {
        padding-top: 40px !important;
        padding-bottom: 20px !important;
    }

    .landing-heading {
        font-size: 52px;
        font-weight: 900;
        line-height: 1.05;
        margin-top: 70px;
    }

    .landing-blue {
        color: #2196F3;
    }

    .landing-subtitle {
        font-size: 22px;
        font-weight: 600;
        margin-top: 20px;
    }

    .landing-description {
        font-size: 17px;
        line-height: 1.7;
        margin-top: 15px;
        color: #c8c8c8;
    }

    .feature-text {
        font-size: 16px;
        margin-top: 15px;
    }

    </style>
    """, unsafe_allow_html=True)


    # =====================================================
    # TWO COLUMN LAYOUT
    # =====================================================

    left, right = st.columns([1.05, 1])


    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        st.markdown(
            '<div class="landing-heading">'
            'AI <span class="landing-blue">FRAUD</span><br>'
            'DETECTION'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="landing-subtitle">'
            'Smart protection against online fraud'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="landing-description">'
            'Protect yourself from fraudulent messages, '
            'phishing attempts and suspicious links using '
            'an AI-powered fraud detection system.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="feature-text">🧠 &nbsp; AI-Based Message Detection</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">🔗 &nbsp; Suspicious Link Detection</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">📊 &nbsp; Risk Score & Analysis</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">🛡️ &nbsp; Secure & Easy to Use</div>',
            unsafe_allow_html=True
        )

        # Space before button
        st.write("")
        st.write("")
        st.write("")

        # =================================================
        # ENTER SYSTEM BUTTON
        # =================================================

        if st.button(
            "ENTER SYSTEM  →",
            key="enter_system_button",
            use_container_width=False
        ):
            st.session_state["entered_system"] = True
            st.rerun()


    # =====================================================
    # RIGHT SIDE - ROBOT IMAGE
    # =====================================================

    with right:

        st.write("")
        st.write("")

        st.image(
            "robot_circle.png",
            width=450
        )
    

# =========================================================
# PAGE 2 - LOGIN / REGISTER
# =========================================================

elif not st.session_state["logged_in"]:

    st.markdown("")

    # Page title
    st.markdown(
        "<h1 style='text-align:center; "
        "font-size:40px; "
        "font-weight:800; "
        "color:white;'>"
        "🛡️ AI FRAUD DETECTION"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; "
        "font-size:17px; "
        "color:#c7d7e5 !important;'>"
        "Secure access to your AI-powered fraud detection system"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # =====================================================
    # LOGIN / REGISTER CARD
    # =====================================================

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.write("")

        tab1, tab2 = st.tabs(
            ["🔐 Login", "📝 Register"]
        )

        # =================================================
        # LOGIN
        # =================================================

        with tab1:

            st.subheader("User Login")

            username = st.text_input(
                "Username",
                key="login_username"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button(
                "🔐 LOGIN",
                key="login_button",
                use_container_width=True
            ):

                if username.strip() == "" or password == "":

                    st.warning(
                        "Please enter username and password."
                    )

                elif login_user(
                    username.strip(),
                    password
                ):

                    st.session_state["logged_in"] = True

                    st.session_state["username"] = (
                        username.strip()
                    )

                    st.success(
                        "Login successful! ✅"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid username or password."
                    )


        # =================================================
        # REGISTER
        # =================================================

        with tab2:

            st.subheader("Create New Account")

            new_username = st.text_input(
                "Choose Username",
                key="register_username"
            )

            new_password = st.text_input(
                "Choose Password",
                type="password",
                key="register_password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="confirm_password"
            )

            if st.button(
                "📝 REGISTER",
                key="register_button",
                use_container_width=True
            ):

                if new_username.strip() == "":

                    st.warning(
                        "Please enter a username."
                    )

                elif new_password == "":

                    st.warning(
                        "Please enter a password."
                    )

                elif new_password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                elif len(new_password) < 6:

                    st.warning(
                        "Password must contain at least 6 characters."
                    )

                elif register_user(
                    new_username.strip(),
                    new_password
                ):

                    st.success(
                        "Registration successful! "
                        "You can now login."
                    )

                else:

                    st.error(
                        "Username already exists."
                    )


# =========================================================
# PAGE 3 - MAIN SYSTEM
# =========================================================

else:

    # =====================================================
    # YOUR EXISTING DASHBOARD CODE STARTS HERE
    # =====================================================

    st.sidebar.title("🛡️ Fraud Detection")

    st.sidebar.write(
        f"👤 User: {st.session_state['username']}"
    )

    menu = st.sidebar.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "🔍 Message Detection",
            "🔗 Link Detection",
            "📜 Detection History"
        ]
    )

    if st.sidebar.button("🚪 Logout"):

        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["entered_system"] = False

        st.rerun()


    # =====================================================
    # HOME DASHBOARD
    # =====================================================

    if menu == "🏠 Dashboard":

        st.title(
            "🛡️ AI Fraud Detection Dashboard"
        )

        st.success(
            f"Welcome, {st.session_state['username']}! 👋"
        )
                # ==============================
        # DETECTION STATISTICS
        # ==============================

        history = get_history(
            st.session_state["username"]
        )

        total_detections = len(history)

        fraud_count = sum(
            1 for item in history
            if item[1] == "Fraud"
        )

        safe_count = sum(
            1 for item in history
            if item[1] == "Safe"
        )

        if total_detections > 0:
            average_risk = sum(
                item[2] for item in history
            ) / total_detections
        else:
            average_risk = 0

        st.subheader("📊 Detection Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Detections",
                total_detections
            )

        with col2:
            st.metric(
                "🚨 Fraud Detected",
                fraud_count
            )

        with col3:
            st.metric(
                "✅ Safe Messages",
                safe_count
            )

        with col4:
            st.metric(
                "⚠️ Avg. Risk",
                f"{average_risk:.1f}%"
            )

        st.divider()

        st.subheader("System Features")

        col1, col2 = st.columns(2)

        with col1:

            st.info("📩 Message Detection")

            st.write(
                "Analyze messages using the AI model."
            )

        with col2:

            st.info("📊 Risk Score")

            st.write(
                "Get a risk percentage for detected messages."
            )

        st.divider()

        st.subheader("🔐 Security")

        st.write(
            "User authentication is protected using "
            "password hashing and SQLite database."
        )


    # =====================================================
    # MESSAGE DETECTION
    # =====================================================

    elif menu == "🔍 Message Detection":

        st.title(
            "🔍 Fraud Message Detection"
        )

        st.write(
            "Enter a message below to check "
            "whether it may be fraudulent."
        )

        message = st.text_area(
            "📩 Enter Message",
            placeholder=(
                "Example: Congratulations! "
                "You won a prize. "
                "Click the link to claim it."
            )
        )

        if st.button("🔎 Detect Fraud"):

            if message.strip() == "":

                st.warning(
                    "Please enter a message."
                )

            else:

                try:

                    # Load trained model
                    with open(
                        "model.pkl",
                        "rb"
                    ) as file:

                        model = pickle.load(file)

                    # AI prediction
                    prediction = model.predict(
                        [message]
                    )[0]

                    # Probability
                    probability = model.predict_proba(
                        [message]
                    )[0]

                    # Fraud probability
                    fraud_score = probability[1] * 100

                    # ---------------- RISK LEVEL ----------------
                    if prediction == 0:
                        if fraud_score <= 30:
                            risk_level = "🟢 Low Risk"
                        else:
                            risk_level = "🟢 Safe / Low Risk"
                    else:
                        if fraud_score <= 70:
                            risk_level = "🟡 Medium Risk"
                        else:
                            risk_level = "🔴 High Risk"



                    # ---------------- RESULT ----------------

                    if prediction == 1:

                        result = "Fraud"

                        st.error(
                            "🚨 FRAUDULENT MESSAGE DETECTED"
                        )
                        st.subheader("🔎 Why is this message suspicious?")

                        reasons = []

                        lower_message = message.lower()

                        if "click" in lower_message or "link" in lower_message:
                            reasons.append("🔗 Contains a link or asks you to click something.")

                        if "urgent" in lower_message or "immediately" in lower_message:
                            reasons.append("⚠️ Uses urgent or pressure-based language.")

                        if "prize" in lower_message or "reward" in lower_message or "lottery" in lower_message:
                            reasons.append("💰 Mentions a prize, reward, or lottery.")

                        if "verify" in lower_message or "verification" in lower_message:
                            reasons.append("🔐 Requests account or identity verification.")

                        if "win" in lower_message or "won" in lower_message:
                            reasons.append("🎁 Claims that you have won something.")

                        if reasons:
                            for reason in reasons:
                                st.write(reason)
                        else:
                            st.write("⚠️ The AI model identified this message as suspicious.")

                        st.warning(
                            "⚠️ This message may contain "
                            "phishing or scam content. "
                            "Avoid clicking suspicious links "
                            "or sharing personal information."
                        )
                        st.divider()

                        st.subheader("🛡️ Safety Tips")

                        st.write(
                            "• Do not click links from unknown senders."
                        )

                        st.write(
                            "• Never share OTPs, passwords, or PINs."
                        )

                        st.write(
                            "• Verify the sender before making payments."
                        )

                        st.write(
                            "• Be careful with urgent prize or reward messages."
                        )

                        st.write(
                            "• Use official websites or apps for account verification."
                        )

                        st.subheader("🛡️ Safety Tips")

                        st.write(
                            "• Do not click links from unknown senders."
                        )

                        st.write(
                            "• Never share OTPs, passwords, or PINs."
                        )

                        st.write(
                            "• Verify the sender before making payments."
                        )

                        st.write(
                            "• Be careful with urgent prize or reward messages."
                        )

                        st.write(
                            "• Use official websites or apps for account verification."
                        )

                    else:

                        result = "Safe"

                        st.success(
                            "✅ MESSAGE APPEARS SAFE"
                        )

                        st.info(
                            "This message does not appear "
                            "to contain obvious fraudulent patterns."
                        )


                    # ---------------- SCORE ----------------

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "📊 Risk Score",
                            f"{fraud_score:.1f}%"
                        )

                    with col2:

                        st.metric(
                            "⚠️ Risk Level",
                            risk_level
                        )
                        


                    # ---------------- SAVE HISTORY ----------------

                    save_detection(
                        st.session_state["username"],
                        message,
                        result,
                        fraud_score
                    )


                except FileNotFoundError:

                    st.error(
                        "model.pkl not found. "
                        "Please train the model first."
                    )

                except Exception as e:

                    st.error(
                        f"An error occurred: {e}"
                    )
                        # =====================================================
    # LINK DETECTION
    # =====================================================

    elif menu == "🔗 Link Detection":

        st.title("🔗 Fraud Link Detection")

        st.write(
            "Analyze a website URL using machine learning "
            "and security-based URL characteristics."
        )

        st.divider()

        url = st.text_input(
            "🌐 Enter Website URL",
            placeholder="Example: https://example.com/login",
            key="url_input"
        )

        if st.button(
            "🔎 ANALYZE LINK",
            key="analyze_link_button",
            use_container_width=True
        ):

            if url.strip() == "":
                st.warning("Please enter a website URL.")

            else:

                try:

                    # =================================================
                    # LOAD URL MODEL
                    # =================================================

                    with open("url_model.pkl", "rb") as file:
                        url_model = pickle.load(file)


                    # =================================================
                    # URL FEATURE EXTRACTION
                    # =================================================

                    import re
                    from urllib.parse import urlparse

                    url_text = url.strip().lower()

                    analysis_url = url_text

                    if not analysis_url.startswith(
                        ("http://", "https://")
                    ):
                        analysis_url = "https://" + analysis_url

                    parsed_url = urlparse(analysis_url)

                    domain = parsed_url.netloc.lower()

                    url_length = len(url_text)


                    # =================================================
                    # IP ADDRESS DETECTION
                    # =================================================

                    has_ip = 1 if re.fullmatch(
                        r"\d{1,3}(\.\d{1,3}){3}",
                        domain.split(":")[0]
                    ) else 0


                    # =================================================
                    # HTTPS DETECTION
                    # =================================================

                    has_https = (
                        1
                        if parsed_url.scheme == "https"
                        else 0
                    )


                    # =================================================
                    # SUSPICIOUS KEYWORDS
                    # =================================================

                    suspicious_words = [
                        "login",
                        "verify",
                        "verification",
                        "account",
                        "update",
                        "urgent",
                        "claim",
                        "password",
                        "bank",
                        "secure",
                        "signin",
                        "confirm",
                        "wallet",
                        "payment"
                    ]

                    found_keywords = [
                        word
                        for word in suspicious_words
                        if word in url_text
                    ]

                    suspicious_count = len(found_keywords)


                    # =================================================
                    # URL STRUCTURE FEATURES
                    # =================================================

                    dot_count = url_text.count(".")

                    slash_count = url_text.count("/")

                    special_count = sum(
                        char in "@?=&_%"
                        for char in url_text
                    )

                    hyphen_count = url_text.count("-")

                    domain_parts = domain.split(".")

                    subdomain_count = max(
                        len(domain_parts) - 2,
                        0
                    )


                    # =================================================
                    # URL SHORTENER DETECTION
                    # =================================================

                    shortener_domains = [
                        "bit.ly",
                        "tinyurl.com",
                        "t.co",
                        "is.gd",
                        "cutt.ly",
                        "shorturl.at"
                    ]

                    is_shortened = any(
                        domain == item
                        or domain.endswith("." + item)
                        for item in shortener_domains
                    )


                    # =================================================
                    # AI MODEL PREDICTION
                    # =================================================

                    features = [[
                        url_length,
                        has_ip,
                        has_https,
                        suspicious_count,
                        dot_count,
                        slash_count,
                        special_count
                    ]]

                    prediction = url_model.predict(
                        features
                    )[0]


                    # =================================================
                    # ML RISK SCORE
                    # =================================================

                    if hasattr(
                        url_model,
                        "predict_proba"
                    ):

                        probabilities = (
                            url_model.predict_proba(features)[0]
                        )

                        if len(probabilities) > 1:

                            ml_score = (
                                probabilities[1] * 100
                            )

                        else:

                            ml_score = 0

                    else:

                        ml_score = (
                            80
                            if prediction == 1
                            else 20
                        )


                    # =================================================
                    # SECURITY INDICATOR SCORE
                    # =================================================

                    security_score = 0

                    risk_reasons = []


                    if has_ip:

                        security_score += 25

                        risk_reasons.append(
                            "🌐 IP address used instead of a normal domain."
                        )


                    if not has_https:

                        security_score += 15

                        risk_reasons.append(
                            "🔓 Connection does not use HTTPS."
                        )


                    if url_length > 75:

                        security_score += 15

                        risk_reasons.append(
                            "📏 URL is unusually long."
                        )


                    if suspicious_count >= 2:

                        security_score += 20

                        risk_reasons.append(
                            "⚠️ Multiple suspicious keywords detected."
                        )

                    elif suspicious_count == 1:

                        security_score += 8

                        risk_reasons.append(
                            "⚠️ Potentially sensitive keyword detected."
                        )


                    if dot_count > 3:

                        security_score += 10

                        risk_reasons.append(
                            "🔗 URL contains many dots or subdomains."
                        )


                    if special_count > 3:

                        security_score += 10

                        risk_reasons.append(
                            "⚠️ URL contains several special characters."
                        )


                    if subdomain_count >= 3:

                        security_score += 10

                        risk_reasons.append(
                            "🌐 Multiple subdomain levels detected."
                        )


                    if is_shortened:

                        security_score += 15

                        risk_reasons.append(
                            "🔗 URL uses a URL-shortening service."
                        )


                    if hyphen_count >= 3:

                        security_score += 5

                        risk_reasons.append(
                            "⚠️ Domain contains several hyphens."
                        )


                    # =================================================
                    # FINAL RISK SCORE
                    # =================================================

                    final_score = (
                        (ml_score * 0.55)
                        +
                        (security_score * 0.45)
                    )

                    final_score = max(
                        0,
                        min(100, final_score)
                    )


                    # =================================================
                    # RISK CLASSIFICATION
                    # =================================================

                    if (
                        has_ip
                        or suspicious_count >= 2
                        or security_score >= 40
                    ):

                        risk_level = "🔴 HIGH RISK"

                        risk_message = (
                            "This URL contains multiple suspicious "
                            "characteristics and should be treated "
                            "with caution."
                        )

                    elif (
                        suspicious_count == 1
                        or security_score >= 20
                    ):

                        risk_level = "🟡 MEDIUM RISK"

                        risk_message = (
                            "This URL contains some characteristics "
                            "that require caution."
                        )

                    else:

                        risk_level = "🟢 LOW RISK"

                        risk_message = (
                            "No major suspicious URL characteristics "
                            "were detected."
                        )


                    # =================================================
                    # RESULT
                    # =================================================

                    if risk_level == "🔴 HIGH RISK":

                        st.error(
                            "🚨 RISKY LINK DETECTED"
                        )

                    elif risk_level == "🟡 MEDIUM RISK":

                        st.warning(
                            "⚠️ POTENTIALLY RISKY LINK"
                        )

                    else:

                        st.success(
                            "🛡️ LOW-RISK LINK"
                        )


                    # =================================================
                    # SCORE CARDS
                    # =================================================

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "📊 Risk Score",
                            f"{final_score:.1f}%"
                        )

                    with col2:

                        st.metric(
                            "🛡️ Security Level",
                            risk_level
                        )


                    st.progress(
                        int(final_score)
                    )

                    st.info(
                        risk_message
                    )

                    # Save this URL detection for the logged-in user.
                    save_detection(
                        st.session_state["username"],
                        url.strip(),
                        risk_level,
                        final_score,
                        detection_type="Link"
                    )

                    # =================================================
                    # URL ANALYSIS
                    # =================================================

                    st.subheader("🌐 URL Analysis")

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.write("**Protocol**")

                        st.write(
                            parsed_url.scheme.upper()
                        )

                    with col2:

                        st.write("**Domain**")

                        st.write(
                            domain
                            if domain
                            else "Unknown"
                        )

                    with col3:

                        st.write("**URL Length**")

                        st.write(
                            f"{url_length} characters"
                        )


                    # =================================================
                    # SECURITY INDICATORS
                    # =================================================

                    st.subheader(
                        "🔎 Security Indicators"
                    )

                    if risk_reasons:

                        for reason in risk_reasons:

                            st.write(reason)

                    else:

                        st.success(
                            "✅ No significant URL-level "
                            "warning indicators were found."
                        )


                    # =================================================
                    # AI MODEL ASSESSMENT
                    # =================================================

                    st.subheader(
                        "🤖 AI Model Assessment"
                    )

                    if prediction == 1:

                        st.write(
                            "The machine-learning model classified "
                            "this URL as suspicious."
                        )

                    else:

                        st.write(
                            "The machine-learning model did not "
                            "classify this URL as suspicious."
                        )


                    # =================================================
                    # SECURITY RECOMMENDATIONS
                    # =================================================

                    st.subheader(
                        "🛡️ Security Recommendations"
                    )

                    if risk_level == "🔴 HIGH RISK":

                        st.write(
                            "🚫 Avoid opening or interacting with this URL."
                        )

                        st.write(
                            "🔐 Do not enter passwords, OTPs, PINs, "
                            "or banking information."
                        )

                        st.write(
                            "🌐 Access the service through its official "
                            "website or application."
                        )

                        st.write(
                            "📩 Verify the sender if the URL was received "
                            "through a message or email."
                        )

                    elif risk_level == "🟡 MEDIUM RISK":

                        st.write(
                            "⚠️ Verify the domain before continuing."
                        )

                        st.write(
                            "🔐 Avoid entering sensitive information."
                        )

                        st.write(
                            "🌐 Prefer accessing the service through "
                            "the official website."
                        )

                    else:

                        st.write(
                            "✅ No major URL-level warning signs detected."
                        )

                        st.write(
                            "🔎 Still verify the domain before entering "
                            "sensitive information."
                        )

                        st.write(
                            "🔐 Never share OTPs, passwords, "
                            "or banking credentials."
                        )


                    st.caption(
                        "Security note: A low-risk result does not "
                        "guarantee that a website is completely safe. "
                        "This system performs URL-based risk assessment."
                    )


                except FileNotFoundError:

                    st.error(
                        "❌ url_model.pkl not found. "
                        "Please create and train the URL model first."
                    )

                except Exception as e:

                    st.error(
                        f"Unable to analyze this URL: {e}"
                    )


    # =====================================================
    # DETECTION HISTORY
    # =====================================================

    elif menu == "📜 Detection History":

        st.title("📜 Detection History")
        st.caption("View your message and link checks separately.")

        history = get_history(st.session_state["username"])
        message_history = [
            item for item in history
            if len(item) < 5 or item[4] == "Message"
        ]
        link_history = [
            item for item in history
            if len(item) >= 5 and item[4] == "Link"
        ]

        message_tab, link_tab = st.tabs([
            f"🔍 Message History ({len(message_history)})",
            f"🔗 Link History ({len(link_history)})"
        ])

        with message_tab:
            if message_history:
                for msg, result, score, date, *extra in message_history:
                    with st.container(border=True):
                        st.write("📩 **Message**")
                        st.write(msg)
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write("📌 **Result**")
                            st.write(result)
                        with col2:
                            st.write("📊 **Risk Score**")
                            st.write(f"{score:.1f}%")
                        with col3:
                            st.write("🕐 **Date & Time**")
                            st.write(date)
            else:
                st.info("No message detection history available yet.")

        with link_tab:
            if link_history:
                for url_text, result, score, date, *extra in link_history:
                    with st.container(border=True):
                        st.write("🌐 **Checked URL**")
                        st.code(url_text, language=None)
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write("📌 **Risk Level**")
                            st.write(result)
                        with col2:
                            st.write("📊 **Risk Score**")
                            st.write(f"{score:.1f}%")
                        with col3:
                            st.write("🕐 **Date & Time**")
                            st.write(date)
            else:
                st.info("No link detection history available yet.")
