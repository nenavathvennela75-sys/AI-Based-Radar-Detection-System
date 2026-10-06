import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI-Based Radar System",
    page_icon="📡",
    layout="wide"
)

st.title("📡 AI-Based Radar System")
st.write("Radar object detection and visualization")

# -----------------------------
# User Inputs
# -----------------------------
st.sidebar.header("Radar Settings")

angle = st.sidebar.slider(
    "Radar Angle",
    min_value=0,
    max_value=180,
    value=90
)

distance = st.sidebar.slider(
    "Object Distance (cm)",
    min_value=10,
    max_value=200,
    value=100
)

# -----------------------------
# Object Detection
# -----------------------------
if distance < 50:
    object_status = "🚨 Object Detected - Very Close"
elif distance < 100:
    object_status = "⚠️ Object Detected"
else:
    object_status = "✅ No Nearby Object"

# -----------------------------
# Radar Calculation
# -----------------------------
theta = np.radians(angle)

x = distance * np.cos(theta)
y = distance * np.sin(theta)

# -----------------------------
# Radar Display
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 5))

# Radar semicircle
radar_angles = np.linspace(0, np.pi, 200)

for radius in [50, 100, 150, 200]:
    ax.plot(
        radius * np.cos(radar_angles),
        radius * np.sin(radar_angles),
        linestyle="--",
        linewidth=0.8
    )

# Radar boundary
ax.plot(
    200 * np.cos(radar_angles),
    200 * np.sin(radar_angles),
    linewidth=2
)

# Radar scanning line
ax.plot(
    [0, x],
    [0, y],
    linewidth=2
)

# Detected object
if distance < 150:
    ax.scatter(
        x,
        y,
        s=150,
        marker="o"
    )

# Display settings
ax.set_xlim(-210, 210)
ax.set_ylim(0, 210)
ax.set_aspect("equal")

ax.set_xlabel("X Position (cm)")
ax.set_ylabel("Y Position (cm)")
ax.set_title("Radar Detection Screen")

st.pyplot(fig)

# -----------------------------
# Information
# -----------------------------
st.subheader("Detection Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Angle", f"{angle}°")

with col2:
    st.metric("Distance", f"{distance} cm")

with col3:
    st.write(object_status)