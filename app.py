import streamlit as st

# --- Simple Login Logic ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "sudip" and password == "bohara123":
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid credentials. Try again.")

def logout():
    st.session_state.authenticated = False
    st.rerun()

# --- Show login screen if not authenticated ---
if not st.session_state.authenticated:
    login()
    st.stop() # stop rest of the app from running

# --- Add logout button ---
st.sidebar.markdown("---")
st.sidebar.button("Logout", on_click=logout)


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Course", "Contact", "About Us","Gallery",
                                  "Products/Services","News/Blog","Tech Reviews","Deals/Discounts"])


# --- Home Page ---
if page == "Home":
    st.title("Welcome to Our Site")
    st.write("This is the **Home** page.")
    st.write("Explore the menu to learn more about our courses or get in touch!")

    # Example: Showcase courses or news
    st.subheader("Latest Updates")
    st.info("🎉 New course launching next week — stay tuned!")

# --- Course Page ---
elif page == "Course":
    st.title("Our Courses")
    st.write("This is the **Course** page. Here’s a preview of what we offer:")

    courses = [
        {"title": "Python 101", "description": "Introductory Python programming."},
        {"title": "Data Science Basics", "description": "Learn data analysis & visualization."},
        {"title": "Web Apps with Streamlit", "description": "Build interactive web apps in Python."},
    ]
    for c in courses:
        st.markdown(f"### {c['title']}")
        st.write(c['description'])
        st.button(f"Enroll in {c['title']}")

# --- Contact Page ---
elif page == "Contact":
    st.title("Contact Us")
    st.write("Got questions? Drop us a message below!")
    name = st.text_input("Your Name", placeholder="Type your name here")
    email = st.text_input("Your Email", placeholder="you@example.com")
    message = st.text_area("Message", placeholder="Write your message here...")

    if st.button("Send Message"):
        # Demo confirmation message
        st.success(f"Thanks {name}! Your message has been sent.")
        st.write("We’ll get back to you at", email)
        # In a real app, you'd handle the form submission here.

# --- About Us Page ---
elif page == "About Us":
    st.title("🙋‍♂️ About Us")
    st.write("""
        Welcome to our demo website!  
        We are a small team passionate about **education**, **technology**, and making learning accessible for everyone.
        
        Our mission is to:
        - Simplify complex topics with clear, hands-on courses.
        - Empower beginners to build real-world skills.
        - Foster a community of continuous learners.

        Whether you're just getting started or looking to sharpen your skills, we’re here to help.
    """)


# --- Gallery Page ---
elif page == "Gallery":
    st.title("🖼️ Gallery")
    st.write("Enjoy a selection of random images showcased below:")

    images = [
        "images/1.jpg",
        "images/2.jpg",
        "images/3.jpg",
        "images/4.webp"
    ]
    captions = ["Random Image 1", "Random Image 2", "Random Image 3", "Random Image 4"]
    st.image(images, caption=captions, width=300)

# --- Products/Services Page ---
elif page == "Products/Services":
    st.title("🛍️ Products & Services")
    st.write("Browse our tech products and services:")

    products = [
        {
            "name": "AI Chatbot",
            "description": "Smart virtual assistant for your website.",
            "price": "$199",
            "image": "images/ai.webp"
        },
        {
            "name": "Custom Web App",
            "description": "We build web apps with Python, Streamlit & Flask.",
            "price": "Starting at $499",
            "image": "images/website.jpg"
        },
        {
            "name": "Data Analysis Service",
            "description": "Visual reports + insights from your data.",
            "price": "$149",
            "image": "images/data_analysis.png"
        },
        {
            "name": "1-on-1 Mentorship",
            "description": "Get private training in coding & projects.",
            "price": "$39/hr",
            "image": "images/all-in-one.jpg"
        }
    ]

    for p in products:
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(p["image"], width=140)
        with cols[1]:
            st.markdown(f"### {p['name']}")
            st.write(p["description"])
            st.markdown(f"**Price**: {p['price']}")
            st.button(f"Inquire about {p['name']}")
# ---- Deals/Discounts ----
elif page == "Deals/Discounts":
    st.title("💸 Deals & Discounts on Courses")
    st.subheader("🔥 Limited Time Offers on Popular Courses")

    deals = [
        {
            "course": "Python 101",
            "original_price": "$99",
            "discounted_price": "$49",
            "validity": "Valid till June 30, 2025",
            "image": "images/python-ai.webp"
        },
        {
            "course": "Data Science Basics",
            "original_price": "$149",
            "discounted_price": "$89",
            "validity": "Valid till July 5, 2025",
            "image": "images/data-science.jpg"
        },
        {
            "course": "Streamlit Web App",
            "original_price": "$129",
            "discounted_price": "$69",
            "validity": "Valid till July 10, 2025",
            "image": "images/striamlit.png"
        }
    ]

    for deal in deals:
        st.markdown("----")
        st.image(deal["image"], width=400)
        st.markdown(f"### {deal['course']}")
        st.markdown(f"💲 Original: ~~{deal['original_price']}~~")
        st.markdown(f"✅ Now: **{deal['discounted_price']}**")
        st.caption(f"🕒 {deal['validity']}")
        st.button(f"Get Deal for {deal['course']}")

# ----- News/Blog ---- 
elif page == "News/Blog":
    st.title("📰 Tech News / Blog")
    st.write("Check out our latest articles and updates from the tech world!")

    blogs = [
        {
            "title": "AI is Changing the World",
            "date": "June 25, 2025",
            "summary": "Discover how AI is transforming industries and jobs.",
            "image": "images/ai-img.jpeg"
        },
        {
            "title": "Why Learn Python in 2025?",
            "date": "June 20, 2025",
            "summary": "Python continues to lead in automation, data, and AI.",
            "image": "images/python-ai.webp"
        }
    ]
    for blog in blogs:
        st.image(blog["image"], use_column_width=True)
        st.markdown(f"### {blog['title']}")
        st.caption(blog["date"])
        st.write(blog["summary"])
        st.markdown("---")


# ---- Tech Reviews -----
elif page == "Tech Reviews":
    st.title("💻 Tech Reviews")
    st.write("Honest reviews of the latest tech gadgets and tools:")

    reviews = [
        {
            "product": "AI Chatbot",
            "rating": "⭐⭐⭐⭐½",
            "review": "Blazing fast for data work and coding. Battery life is excellent.",
            "image": "images/ai.webp"
        },
        {
            "product": "Custom Web App",
            "rating": "⭐⭐⭐⭐⭐",
            "review": "One of the best productivity mice for developers and designers.",
            "image": "images/website.jpg"
        }
    ]

    for r in reviews:
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(r["image"], width=150)
        with cols[1]:
            st.markdown(f"### {r['product']}")
            st.write(r["review"])
            st.markdown(f"**Rating**: {r['rating']}")
            st.markdown("---")

# ---- Deals/Discounts ----
elif page == "Deals/Discounts":
    st.title("💸 Deals & Discounts on Courses")
    st.subheader("🔥 Limited Time Offers on Popular Courses")

    deals = [
        {
            "course": "Python 101",
            "original_price": "$99",
            "discounted_price": "$49",
            "validity": "Valid till June 30, 2025",
            "image": "images/python-ai.webp"
        },
        {
            "course": "Data Science Basics",
            "original_price": "$149",
            "discounted_price": "$89",
            "validity": "Valid till July 5, 2025",
            "image": "images/data-science.jpg"
        },
        {
            "course": "Streamlit Web App",
            "original_price": "$129",
            "discounted_price": "$69",
            "validity": "Valid till July 10, 2025",
            "image": "images/striamlit.png"
        }
    ]

    for deal in deals:
        st.markdown("----")
        st.image(deal["image"], width=400)
        st.markdown(f"### {deal['course']}")
        st.markdown(f"💲 Original: ~~{deal['original_price']}~~")
        st.markdown(f"✅ Now: **{deal['discounted_price']}**")
        st.caption(f"🕒 {deal['validity']}")
        st.button(f"Get Deal for {deal['course']}")

# --- Footer ---
st.markdown("---")
st.write("© 2025 Demo Site")


