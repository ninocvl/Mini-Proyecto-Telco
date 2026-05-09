import gradio as gr
import requests

API_URL = "https://telco-churn-api-sseb.onrender.com/predict"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

:root {
    --bg:          #151210;
    --surface:     #1c1814;
    --border:      #2e2824;
    --border-dark: #3a332d;
    --text:        #e8e2d9;
    --text-muted:  #9c9189;
    --text-faint:  #5c524a;
    --sage:        #6b8f72;
    --sage-light:  #2a3d2d;
    --rose:        #a67468;
    --rose-light:  #3d2420;
    --sand:        #a68c6a;
    --sand-light:  #3d2e1e;
    --ink:         #e8e2d9;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── FULL WIDTH RESET ── */
html, body {
    background: var(--bg) !important;
    width: 100% !important;
    
}

.gradio-container,
.gradio-container > *,
footer {
    background: var(--bg) !important;
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    box-shadow: none !important;
    border: none !important;
    
}

/* hide gradio footer */
footer { display: none !important; }

/* ── WRAPPER ── */
.wrap {
    max-width: 1080px;
    margin: 0 auto;
    padding: rem;
}

/* ── TOP BAR ── */
.topbar {
    width: 100%;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0;
    margin-top: 2rem;
    padding: 0.75rem 0.5rem;
}

.topbar-inner {
    max-width: 1080px;
    margin: 0 auto;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
}

.topbar-title {
    font-family: 'Poppins', serif !important;
    font-size: 1.35rem !important;
    font-weight: 400 !important;
    color: var(--ink) !important;
    letter-spacing: -0.01em;
    margin: 0 !important;
}

.topbar-meta {
    font-family: 'Poppins', sans-serif;
    font-size: 0.72rem;
    color: var(--text-faint);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── SECTION LABELS ── */
.section-label {
    font-family: 'Poppins', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border);
}

.section-label svg {
    flex-shrink: 0;
}

/* ── DIVIDER ── */
.divider {
    width: 100%;
    height: 1px;
    background: var(--border);
    margin: 0.5rem 0;
}

/* ── INPUTS ── */
label span,
.gr-form label span {
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    color: var(--text-muted) !important;
    
}

input[type="number"],
input[type="text"],
.gr-input input,
textarea {
    background: var(--surface) !important;
    border: 1px solid var(--border-dark) !important;
    border-radius: 4px !important;
    color: var(--text) !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.88rem !important;
    padding: 0.55rem 0.75rem !important;
    transition: border-color 0.15s !important;
    box-shadow: none !important;
    outline: none !important;
}

input:focus, textarea:focus {
    border-color: var(--sand) !important;
    box-shadow: 0 0 0 2px rgba(196,168,130,0.15) !important;
}

select, .gr-select select,
.wrap select {
    background: var(--surface) !important;
    border: 1px solid var(--border-dark) !important;
    border-radius: 4px !important;
    color: var(--text) !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.88rem !important;
    
}

/* Gradio dropdown list items */
.gr-dropdown .choices__item,
ul.choices__list li {
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.88rem !important;
    color: var(--text) !important;
    background: var(--surface) !important;
}

/* Slider */
input[type="range"] {
    accent-color: var(--sand) !important;
}

/* ── BUTTON ── */
.predict-btn, button.primary, .gr-button-primary {
    background: var(--sand) !important;
    border: none !important;
    border-radius: 4px !important;
    color: #fdfcfb !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    padding: 0.75rem 2rem !important;
    cursor: pointer !important;
    transition: background 0.15s !important;
    width: 100% !important;
    box-shadow: none !important;
    margin-top: 2rem !important;
    
}

.predict-btn:hover, button.primary:hover {
    background: var(--sand-light) !important;
}

/* ── OUTPUT CARD ── */
.result-idle {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 2.5rem 1.5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    min-height: 140px;
    justify-content: center;
}

.result-idle-text {
    font-family: 'Poppins', sans-serif;
    font-size: 0.78rem;
    color: var(--text-faint);
    letter-spacing: 0.05em;
}

.result-card {
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    min-height: 140px;
}

.result-stripe {
    height: 3px;
    width: 100%;
}

.result-body {
    background: var(--surface);
    padding: 1.8rem 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.result-verdict {
    font-family: 'Poppins', serif;
    font-size: 2.4rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    line-height: 1;
}

.result-verdict-sub {
    font-family: 'Poppins', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-faint);
}

.prob-row {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.prob-track {
    height: 3px;
    background: var(--border);
    border-radius: 99px;
    overflow: hidden;
}

.prob-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s ease;
}

.prob-label {
    font-family: 'Poppins', sans-serif;
    font-size: 0.72rem;
    color: var(--text-faint);
    display: flex;
    justify-content: space-between;
}

.prob-pct {
    font-weight: 600;
    color: var(--text-muted);
}

/* ── INFO BLOCK ── */
.info-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1.2rem 1.4rem;
    margin-top: 1rem;
}

.info-block p {
    font-family: 'Poppins', sans-serif;
    font-size: 0.78rem;
    color: var(--text-muted);
    line-height: 1.75;
    margin: 0;
}

.info-block strong {
    color: var(--text);
    font-weight: 600;
}

.stat-row {
    display: flex;
    gap: 1rem;
    margin-top: 0.8rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--border);
}

.stat {
    display: flex;
    flex-direction: column;
    gap: 0.1rem;
}

.stat-val {
    font-family: 'Poppins', serif;
    font-size: 1.2rem;
    color: var(--text);
}

.stat-lbl {
    font-family: 'Poppins', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-faint);
}

/* ── MAIN CONTENT PADDING ── */
.main-content {
    padding: 1.5rem 0 4rem;
    display: flex;
    gap: 3rem;
}

/* ── GRADIO OVERRIDES ── */
.gr-block, .gr-box, .gr-form,
.gr-panel, .contain, .gap {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

.gr-padded { padding: 1rem !important; }

.row-wrap { display: flex !important; flex-wrap: wrap !important; gap: 10rem !important; }

/* forzar fondo oscuro en TODOS los inputs de Gradio */
.gradio-container input,
.gradio-container textarea,
.gradio-container select,
.gradio-container [data-testid="textbox"] input,
.gradio-container [data-testid="number"] input,
.gradio-container .wrap-inner,
.gradio-container .secondary-wrap,
.block input,
.block textarea,
.block select,
input, textarea, select {
    background: var(--surface) !important;
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border-color: var(--border-dark) !important;
    font-family: 'Poppins', sans-serif !important;
}

/* dropdown list desplegada */
.gradio-container ul,
.gradio-container .options,
.gradio-container [role="listbox"],
.gradio-container [role="option"] {
    background: var(--surface) !important;
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border-color: var(--border-dark) !important;
    font-family: 'Poppins', sans-serif !important;
    
    
    
}

.gradio-container [role="option"] {
    display:flex !important;
    gap:0.5rem !important;
    padding:0.2rem 0.5rem !important;
}


/* slider track */
.gradio-container .wrap .head,
.gradio-container input[type="range"]::-webkit-slider-runnable-track {
    background: var(--border-dark) !important;
}

/* autofill del browser que pone azul/blanco */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
    -webkit-box-shadow: 0 0 0 1000px var(--surface) inset !important;
    -webkit-text-fill-color: var(--text) !important;
    caret-color: var(--text) !important;
}

/* eliminar fondos blancos de contenedores internos de Gradio */
.gradio-container .block,
.gradio-container .form,
.gradio-container .box,
.gradio-container .gap,
.gradio-container .container,
.gradio-container > div,
.gradio-container .gr-block,
.gradio-container .gr-box,
.gradio-container .gr-form,
.gradio-container .gr-panel,
.gradio-container .wrap,
.gradio-container .innerContainer,
.gradio-container fieldset,
.gradio-container [class*="block"],
.gradio-container [class*="form"],
.gradio-container [class*="wrap"] {
    background: var(--bg) !important;
    background-color: var(--bg) !important;
    border-color: var(--border) !important;
    box-shadow: none !important;
}

.gradio-container .form {
    padding: 0.4rem 0 !important;
    display: flex !important;
    gap: 1.5rem !important;
    border: none !important;
}

.gradio-container .container {
    font-family: 'Poppins', sans-serif !important;
    
    span {
        font-family: 'Poppins', sans-serif !important;
        margin-bottom: 0.25rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        }
}

.gradio-container .wrap {
    .wrap-inner {
        .secondary-wrap {
                input {
                    padding: 0 0.75rem !important;
                    
                }
                
                .icon-wrap {
                    margin-right: -1.2rem !important;
                    background: transparent !important;
                }
            ]
        }
}


"""

# ── SVG SYMBOLS ─────────────────────────────────────────────────────────
SVG_PERSON = '<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="5" r="3"/><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6"/></svg>'
SVG_SIGNAL = '<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 12h2V8H1zM5 12h2V5H5zM9 12h2V2H9zM13 12h2V6h-2z"/></svg>'
SVG_CARD   = '<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="3" width="14" height="10" rx="1.5"/><path d="M1 7h14"/></svg>'
SVG_CIRCLE = '<svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="#d4cec7" stroke-width="1"><circle cx="14" cy="14" r="10" stroke-dasharray="4 3"/></svg>'


def predict_churn(
    gender, senior_citizen, partner, dependents,
    tenure, phone_service, multiple_lines, internet_service,
    online_security, online_backup, device_protection, tech_support,
    streaming_tv, streaming_movies, contract, paperless_billing,
    payment_method, monthly_charges, total_charges
):
    payload = {
        "gender": gender,
        "SeniorCitizen": int(senior_citizen),
        "Partner": partner,
        "Dependents": dependents,
        "tenure": int(tenure),
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": float(monthly_charges),
        "TotalCharges": float(total_charges),
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        result   = response.json()

        prob     = result.get("churn_probability", 0)
        pred     = result.get("prediction", "No")
        is_churn = str(pred).lower() in ("yes", "1", "true", "churn")
        prob_pct = round(prob * 100, 1)

        stripe_color  = "#c9978a" if is_churn else "#84a98c"
        fill_color    = "#c9978a" if is_churn else "#84a98c"
        verdict_color = "#7a3f35" if is_churn else "#2d4a32"
        verdict_text  = "Likely to churn" if is_churn else "Likely to stay"
        verdict_sub   = "High churn risk detected" if is_churn else "Customer appears retained"

        html = f"""
        <div class="result-card">
            <div class="result-stripe" style="background:{stripe_color};"></div>
            <div class="result-body">
                <div>
                    <div class="result-verdict" style="color:{verdict_color}">{verdict_text}</div>
                    <div class="result-verdict-sub" style="margin-top:0.3rem">{verdict_sub}</div>
                </div>
                <div class="prob-row">
                    <div class="prob-track">
                        <div class="prob-fill" style="width:{prob_pct}%;background:{fill_color};"></div>
                    </div>
                    <div class="prob-label">
                        <span>Churn probability</span>
                        <span class="prob-pct">{prob_pct}%</span>
                    </div>
                </div>
            </div>
        </div>
        """

    except requests.exceptions.Timeout:
        html = """
        <div class="result-idle">
            <div class="result-idle-text">API is warming up &mdash; try again in 30s</div>
        </div>"""
    except Exception as e:
        html = f"""
        <div class="result-idle">
            <div class="result-idle-text">Request failed: {e}</div>
        </div>"""

    return html


# ── LAYOUT ──────────────────────────────────────────────────────────────
TOPBAR = """
<div class="topbar">
  <div class="topbar-inner">
    <span class="topbar-title">Churn Predictor</span>
    <span class="topbar-meta">Telco Customer Intelligence</span>
  </div>
</div>
"""

IDLE_OUTPUT = """
<div class="result-idle">
  <svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="#d4cec7" stroke-width="1">
    <circle cx="14" cy="14" r="10" stroke-dasharray="4 3"/>
  </svg>
  <div class="result-idle-text">Complete the form and run prediction</div>
</div>
"""

with gr.Blocks(css=CSS, title="Churn Predictor") as demo:

    gr.HTML(TOPBAR)

    with gr.Row(elem_classes=["wrap", "main-content"]):

        # ── LEFT ──────────────────────────────────────
        with gr.Column(scale=3):

            # Profile
            gr.HTML(f'<div class="section-label">{SVG_PERSON} Customer Profile</div>')
            with gr.Row(elem_classes=["row-wrap"]):
                gender         = gr.Dropdown(["Female", "Male"],  label="Gender",         value="Female")
                senior_citizen = gr.Dropdown([0, 1],              label="Senior Citizen", value=0)
            with gr.Row(elem_classes=["row-wrap"]):
                partner        = gr.Dropdown(["Yes", "No"],       label="Partner",        value="Yes")
                dependents     = gr.Dropdown(["Yes", "No"],       label="Dependents",     value="No")
            tenure = gr.Slider(0, 72, value=1, step=1, label="Tenure (months)")

            gr.HTML('<div class="divider"></div>')

            # Services
            gr.HTML(f'<div class="section-label">{SVG_SIGNAL} Services</div>')
            with gr.Row(elem_classes=["row-wrap"]):
                phone_service  = gr.Dropdown(["Yes", "No"],                             label="Phone Service",    value="No")
                multiple_lines = gr.Dropdown(["Yes", "No", "No phone service"],         label="Multiple Lines",   value="No phone service")
                internet_service = gr.Dropdown(["DSL", "Fiber optic", "No"],            label="Internet Service", value="DSL")
                
            with gr.Row(elem_classes=["row-wrap"]):
                online_security  = gr.Dropdown(["Yes", "No", "No internet service"],    label="Online Security",  value="No")
                online_backup    = gr.Dropdown(["Yes", "No", "No internet service"],    label="Online Backup",    value="Yes")
                device_protection= gr.Dropdown(["Yes", "No", "No internet service"],   label="Device Protection",value="No")
            with gr.Row(elem_classes=["row-wrap"]):
                tech_support     = gr.Dropdown(["Yes", "No", "No internet service"],    label="Tech Support",     value="No")
                streaming_tv     = gr.Dropdown(["Yes", "No", "No internet service"],    label="Streaming TV",     value="No")
                streaming_movies = gr.Dropdown(["Yes", "No", "No internet service"],        label="Streaming Movies", value="No")
                

            gr.HTML('<div class="divider"></div>')

            # Billing
            gr.HTML(f'<div class="section-label">{SVG_CARD} Billing</div>')
            with gr.Row(elem_classes=["row-wrap"]):
                contract          = gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract",          value="Month-to-month")
                paperless_billing = gr.Dropdown(["Yes", "No"],                              label="Paperless Billing", value="Yes")
                payment_method = gr.Dropdown(
                    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
                    label="Payment Method", value="Electronic check"
                )
            with gr.Row(elem_classes=["row-wrap"]):
                monthly_charges = gr.Number(label="Monthly Charges ($)", value=29.85, precision=2)
                total_charges   = gr.Number(label="Total Charges ($)",   value=29.85, precision=2)

        # ── RIGHT ─────────────────────────────────────
        with gr.Column(scale=2):

            predict_btn = gr.Button("Run Prediction", elem_classes=["predict-btn"])
            output_html = gr.HTML(IDLE_OUTPUT)

            

    predict_btn.click(
        fn=predict_churn,
        inputs=[
            gender, senior_citizen, partner, dependents,
            tenure, phone_service, multiple_lines, internet_service,
            online_security, online_backup, device_protection, tech_support,
            streaming_tv, streaming_movies, contract, paperless_billing,
            payment_method, monthly_charges, total_charges
        ],
        outputs=output_html
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)