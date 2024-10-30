"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],
    
    [r"Bist du ([^\?]*)?", 
     ["Du bist selber {0}.", "Du solltest überlegen ob du nicht {0} bist.", "Danke, ich wusste, dass ich {0} bin."]],
    
    [r"Warum (.*?) (.*?) (.*?) (\w+)?",["Ich weiß nicht warum {1} {2} {3} {0}.", 
                                    "Ich sollte dich fragen warum {1} {2} {3} {0}.",
                                    "Ich glaube nicht dass {1} {2} {3} {0}."]],
    
    [r"Ich möchte (.*)",
     ["Warum möchtest du {0}?", "Bist du dir sicher, dass du {0} möchtest?", "Was willst du mit {0} tun?"]],

    [r"Wer ist (.*)(?<![\?\!\.\,\d\;])",
    ["Ich habe keine Ahnung, wer {0} ist, tut mir leid",
    "Leider darf ich keine personenbezogenen Daten mit Dritten teilen. Ich hoffe, du verstehst das!",
    "Die Frage lautet nicht, wer {0} ist. Lass uns lieber drüber nachdenken, wer DU als Mensch sein möchtest."]],

    [r"(?:Ü|ü|Ue|ue)berse?tz(?:.{0,2})(?<![!?])",
    ["Meine Fremdsprachen-Kenntnisse sind leider so ernüchternd wie die Deinen...", 
    "Ich bin mir bei einem Teil des Textes selbst nicht sicher. Frage lieber einen Freund.",
    "Diesen Text zu übersetzen würde bedeuten ihm die Seele zu rauben. Nicht jede Blume blüht auf jedem Felde..."]],

    [r"verfasse{0,1}|erstelle{0,1}|schreibe{0,1}|formuliere{0,1}",
     ["Aber nur, wenn du mich korrekt zitierst!",
      "Da brauchen wir wohl beide Hilfe bei...",
      "Du möchtest ein Premium-Feature nutzen. Informiere dich über unsere aktuellen Tarife!"]],                             

    [r"Magst du (.*)",
    ["Ja, {0} kann wirklich interessant sein!",
    "Manchmal mag ich {0}, es hängt ganz vom Kontext ab.",
    "Erzähl mir, warum du {0} magst."]],

    [r"Ich fühle mich (.*)",
     ["Warum fühlst du dich {0}?",
    "Seit wann fühlst du dich {0}?",
    "Fühlst du dich oft {0}?"]],

    [r"Kannst du mir bei (.*) helfen",
     ["Was genau möchtest du über {0} wissen?",
    "Wie kann ich dir bei {0} behilflich sein?",
    "Erzähl mir mehr über deine Fragen zu {0}."]]


]


psychobabble.append((r'ich bin (.*)', ["Warum bist du {0}?", "Wie lange bist du schon {0}?"]))


psychobabble.append((r'Was geht', ["nichts und bei dir?"]))


psychobabble.append((r'ich mag (.*)', ["Warum magst du {0}?", "Was gefällt dir besonders an {0}?"]))