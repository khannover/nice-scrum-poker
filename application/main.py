from nicegui import app,ui,run
import uuid

ui.add_head_html('''<script>
const userid = localStorage.getItem('userid') || Math.random().toString(36).substring(7);
localStorage.setItem('userid', userid);
</script>
''')

ui.add_css('''
.flip-card {
  background-color: transparent;
  width: 200px;
  height: 200px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.flip-card:hover .flip-card-inner {
  
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.flip-card-front {
  background-color: #bbb;
  color: black;
}

.flip-card-back {
  background-color: #2980b9;
  color: white;
  transform: rotateY(180deg);
}''')

def svg(number, color='#f7f7f7'):
    return f'''
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <rect x="0" y="0" width="200" height="200" fill="{color}" stroke="#000" stroke-width="3" rx="0" />
  <text x="50%" y="60%" text-anchor="middle" font-family="Arial, sans-serif" font-size="80" fill="#000">
    {number}
  </text>
</svg>
'''


with ui.header().classes("bg-dark "): #violet-text
    ui.label('Scrum Poker').classes('text-4xl font-bold text-center text-[#aa00aa] p-2')

with ui.row():
    reveal_btn = ui.button("Aufdecken", on_click=lambda: ui.run_javascript('''document.querySelectorAll('.flip-card-inner').forEach(e => e.style.transform = 'rotateY(180deg)');''')) \
    .on("mouseup", lambda: calculate_points())
    ui.button("Neu", on_click=lambda: clear_cards())

ui.label("Karten auswählen:").classes("text-2xl font-bold text-center p-2")
input_row = ui.row().classes("w-full")
ui.separator()
ui.label("Ergebnis:").classes("text-2xl font-bold text-center p-2")
result_row = ui.row().classes("w-full")

with input_row:
    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(0, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(0, '#ffffff'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg("1/2", '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(0.5, '#ffffff'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(1, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(1, '#00ff00'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(2, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(2, '#33aa11'))


    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(3, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(3, '#76971b'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(5, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(5, '#d6d200'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(8, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(8, '#fc7200'))

    ui.html(f'''
    <div class="flip-card">
      <div class="flip-card-inner2">
        <div class="flip-card-front">
          {svg(13, '#fff')}
        </div>
        <div class="flip-card-back">
          
        </div>
      </div>
    </div>
    ''').on("click", lambda: add_card(13, '#fc1900'))


def add_card(number, color):
    app.storage.general["points"] += number
    app.storage.general["cards"] += 1
    element_id = str(uuid.uuid4())
    with result_row:

        ui.html(f'''
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <img id="{element_id}" src="https://robohash.org/{element_id}.png" alt="Avatar" style="width:200px;height:200px;">
            </div>
            <div class="flip-card-back">
              {svg(number, color)}
            </div>
          </div>
        </div>
        ''')



# calulate the scrum points over all cards
def calculate_points():
    reveal_btn.classes(add="hidden")
    recommendation = ""
    # round up to next fibonacci number
    try:
        average = app.storage.general["points"] / app.storage.general["cards"]
    except ZeroDivisionError:
        average = 0
    if average == 0:
        recommendation = 0
    elif average <= 0.5:
        recommendation = 0.5
    elif average <= 1:
        recommendation = 1
    elif average <= 2:
        recommendation = 2
    elif average <= 3:
        recommendation = 3
    elif average <= 5:
        recommendation = 5
    elif average <= 8:
        recommendation = 8
    elif average <= 13:
        recommendation = 13
    else:
        recommendation = 20

    with result_row:
        ui.label(f'Empfehlung: {recommendation}').classes("text-2xl font-bold text-center p-2")


def clear_cards():
    reveal_btn.classes(remove="hidden")
    result_row.clear()
    app.storage.general["points"] = 0
    app.storage.general["cards"] = 0

app.storage.general["points"] = 0
app.storage.general["cards"] = 0

ui.run(
    port=9999,
    dark=True,
    storage_secret='my_secret',
    title='Nice Scrum Poker',
    favicon="♠️",
)