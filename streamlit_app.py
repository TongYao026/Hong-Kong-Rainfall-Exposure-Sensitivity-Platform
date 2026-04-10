import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GEOG 7310 课程演示",
    page_icon="🌧️",
    layout="wide"
)

GEE_URL = "https://ninth-physics-489311-d2.projects.earthengine.app/view/hk-rainfall-exposure-sensitivity"

st.markdown(
    """
    <style>
    .stApp {
      background:
        radial-gradient(circle at 10% 10%, rgba(20, 90, 150, 0.35) 0%, rgba(7, 12, 24, 0) 30%),
        radial-gradient(circle at 90% 25%, rgba(0, 220, 255, 0.15) 0%, rgba(7, 12, 24, 0) 35%),
        linear-gradient(180deg, #070c18 0%, #0a1022 55%, #070b14 100%);
      color: #d8e6ff;
    }
    .block-container {
      padding-top: 1.3rem;
      padding-bottom: 0.4rem;
    }
    .hero {
      border: 1px solid rgba(119, 219, 255, 0.35);
      border-radius: 18px;
      background: linear-gradient(135deg, rgba(14, 32, 64, 0.95), rgba(12, 54, 96, 0.88));
      box-shadow: 0 0 30px rgba(0, 170, 255, 0.15);
      padding: 24px 26px;
      color: #f5fbff;
      margin-bottom: 16px;
    }
    .hero-kicker {
      font-size: 12px;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      color: #94d9ff;
      margin-bottom: 8px;
    }
    .hero-title {
      font-size: 34px;
      font-weight: 700;
      line-height: 1.12;
      margin: 0;
      color: #ffffff;
      text-shadow: 0 0 24px rgba(125, 223, 255, 0.35);
    }
    .hero-sub {
      margin-top: 8px;
      color: #b5dbff;
      font-size: 15px;
    }
    .glass {
      border: 1px solid rgba(117, 173, 255, 0.22);
      border-radius: 16px;
      background: linear-gradient(140deg, rgba(15, 24, 47, 0.85), rgba(10, 17, 34, 0.88));
      box-shadow: 0 8px 24px rgba(5, 10, 25, 0.5);
      padding: 16px 18px;
      margin-bottom: 12px;
    }
    .card-title {
      margin: 0 0 8px 0;
      color: #87d9ff;
      font-size: 18px;
      font-weight: 600;
    }
    .meta-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(120px, 1fr));
      gap: 8px;
      margin-top: 8px;
    }
    .meta-item {
      border: 1px solid rgba(110, 177, 255, 0.2);
      border-radius: 12px;
      padding: 10px;
      background: rgba(10, 23, 45, 0.65);
      font-size: 13px;
      color: #cde8ff;
    }
    .meta-item strong {
      display: block;
      font-size: 17px;
      color: #8fe2ff;
      margin-top: 4px;
    }
    .section-text {
      color: #d3e7ff;
      font-size: 14px;
      line-height: 1.65;
      margin: 0;
    }
    .list-neo {
      margin: 0;
      padding-left: 16px;
      color: #d3e7ff;
      line-height: 1.7;
      font-size: 14px;
    }
    .embed-wrap {
      border: 1px solid rgba(120, 200, 255, 0.3);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 0 28px rgba(0, 146, 255, 0.22);
      background: rgba(7, 15, 30, 0.9);
    }
    .footer-note {
      color: #8fb8de;
      font-size: 12px;
      margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
      <div class="hero-kicker">GEOG 7310 · FINAL PROJECT · GEOINT VISUAL APP</div>
      <h1 class="hero-title">Hong Kong Rainfall Exposure Sensitivity Platform</h1>
      <div class="hero-sub">香港短时强降雨暴露敏感区综合交互平台</div>
    </div>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1.05, 1.95], gap="medium")

with left:
    st.markdown(
        """
        <div class="glass">
          <div class="card-title">Research Overview / 研究概览</div>
          <p class="section-text">
            This project integrates multi-source Earth observation datasets in Google Earth Engine to identify
            high-sensitivity exposure zones under short-duration extreme rainfall in Hong Kong.
            <br>本研究在 GEE 上整合多源数据，识别香港短时强降雨情景下的高暴露敏感区域，
            强调“快速筛查、分区统计、在线交互展示”一体化流程。
          </p>
          <div class="meta-grid">
            <div class="meta-item">Study Area / 研究区<strong>Hong Kong</strong></div>
            <div class="meta-item">Analysis Period / 时段<strong>2024–2025</strong></div>
            <div class="meta-item">District Units / 行政区<strong>18</strong></div>
            <div class="meta-item">Output Layer / 输出<strong>ESI Level 1–5</strong></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass">
          <div class="card-title">Data Sources / 数据源</div>
          <ul class="list-neo">
            <li>GPM IMERG V07: rainfall hazard intensity and accumulation</li>
            <li>Dynamic World V1: built-up exposure mask</li>
            <li>FABDEM: low-lying and slope-based terrain sensitivity</li>
            <li>Hong Kong District Boundary: zonal statistics and ranking</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass">
          <div class="card-title">Methodology / 方法框架</div>
          <ul class="list-neo">
            <li>Event Filtering: representative short-duration heavy rainfall events</li>
            <li>Factor Extraction: rainfall, built-up distribution, low-lying terrain</li>
            <li>Index Fusion: normalized Exposure Sensitivity Index (ESI)</li>
            <li>District Analytics: area, ratio and level-based comparisons</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass">
          <div class="card-title">Key Findings / 关键发现</div>
          <p class="section-text">
            District-level rainfall exposure ranges from roughly 2,995 mm to 4,047 mm, revealing strong spatial heterogeneity.
            High exposure clusters in north and central-west sectors, while southeastern sectors are relatively lower.
            <br>分区统计显示降雨暴露空间差异明显，北部与中西部更高，东南部分区相对较低，为后续 ESI 重点筛查提供依据。
          </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button("Open Public GEE App / 打开公开GEE应用", GEE_URL, use_container_width=True)

    if "projects.earthengine.app" in GEE_URL:
        st.info("Public app link detected. If some map layers fail to load, set all dependent assets to Anyone can read.")
    if "code.earthengine.google.com" in GEE_URL:
        st.warning("Code Editor URL detected. Public visitors may need Google login; use a published App URL instead.")

with right:
    st.markdown(
        """
        <div class="glass" style="padding:14px 14px 10px 14px;">
          <div class="card-title">Interactive Geospatial Application / 交互地理空间应用</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="embed-wrap">', unsafe_allow_html=True)
    components.iframe(GEE_URL, height=1060, scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)
