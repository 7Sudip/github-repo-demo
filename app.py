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
page = st.sidebar.radio("Go to", ["Home", "Course", "Contact", "About Us","Gallery"])


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
        "1.jpg",
        "2.jpg",
        "3.jpg",
        "4.webp"
    ]
    captions = ["Random Image 1", "Random Image 2", "Random Image 3", "Random Image 4"]
    st.image(images, caption=captions, width=300)




