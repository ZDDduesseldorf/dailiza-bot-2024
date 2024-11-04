
"""
Here we collect the chatbot text patterns.
"""

import datetime

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],
    
    [r"Rechne .*",
    ["Ich bin ein schlechter Kopfrechner.",
    "Damit kann ich nicht rechnen ;)"]],
     
    [r"Weshalb (.*?) (.*?) (.*)(?:[?.!]|)",
    ["Ich weiß nicht weshalb {1} {2} {0}.",
    "Ich bin mir nicht sicher, weshalb {1} {2} {0}.",
    "Ich habe mich auch immer gefragt, weshalb {1} {2} {0}."]],
    
    [r"Ich wünsche mir (.*)",
    ["Sich {0} zu wünschen ist Gefährlich.",
    "Pass auf was du dir wünscht.",
    "WAS?! Ich wünsche mir auch {0}! >:("]],

    [r"Ich fühle (.*)",
    ["Warum fühlst du {0}?",
    " Würde dir denn {0} fühlen wirklich helfen?",
    "Bist du sicher, dass du dich {0} fühlst?"]],

    [r"Kannst du (.*)?", 
    ["Ich kann {0} gerne versuchen!",
     "Das kann ich leider nicht machen!",
     "Kannst du nicht selbst {0}?"]],

    [r"[Mm]ein (.*) (.*)",
    ["Warum denkst Du, dass dein {0} {1}?",
     "Wie beeinflusst dein {0} dein Leben?",
     "Hast du mit jemandem über dein {0} gesprochen?"]],

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

    [r"Ich f(ü|ue|u)hle mich (.*)",
    ["Warum fühlst du dich {1}?",
    "Was denkst du, hat dazu geführt, dass du dich {1} fühlst?",
    "Wie lange fühlst du dich schon {1}?"]],

    [r"Ich kann nicht (.*)",
    ["Warum denkst du, dass du {0} nicht kannst?",
    "Hast du schon mal darüber nachgedacht, warum du {0} nicht kannst?",
    "Was hält dich davon ab, {0} zu können?"]],

    [r"Warum passiert mir immer,? (.*)",
    ["Warum glaubst du, dass dir immer {0} passiert?",
    "Meinst du, dass es einen Grund gibt, warum dir immer {0} passiert?",
    "Was würde passieren, wenn {0} nicht mehr vorkäme?"]],

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
    "Erzähl mir mehr über deine Fragen zu {0}."]],

    [r"Ich heiße (.*)",
     ["Schön, dich kennenzulernen, {0}.",
      "{0}? Schöner Name!"]],

    [r"Danke|Vielen Dank",
     ["Ich helfe immer wieder gern!",
      "no problemo",
      "Gerne! Hast du noch andere Fragen?"]],

    [r"Kannst du mir (.*) empfehlen?",
     ["Da gibt es wirklich vieles! Hast du eine Richtung im Kopf?",
      "Aber klar doch! Was genau soll dabei im Vordergrund stehen?",
      "Ich könnte dir was empfehlen.. aber was bringt es, wenn dus eh nicht verstehst?"]],

    [r"Wenn du (.*) mit etwas vergleichen müsstest, was wäre das?",
     ["Wie einen heißen Sommertag – wunderschön und erdrückend!",
      "{0} zu vergleichen ist ja, als würde man versuchen, eine Kuh zum Fliegen zu bringen!",
      "Ich würde sagen, wie ein gutes Buch: Viele Kapitel und plot twists!"]],

    [r"Bist du gut \b(in|im)\b (.*)",
    ["Ich bin unschlagbar- außer wenn das WLAN ausfällt.",
    "In {0}? Natürlich! Ich habe das im Bot-Training mit Sternchen bestanden.",
    "Ich bin ein Bot. Ich bin gut in allem."]],

    [r"Was machst du (.*)",
    ["Ganz viele 0en und 1en schreiben. 01101001 01100011 01101000 00100000 01100010 01101001 01101110 00100000 01101101 11000011 10111100 01100100 01100101 00100000 00111100 00110011",
    "Das ist natürlich ein Geheimnis :)",
    "Ich tu einfach so, als ob ich ein Chatbot wäre. Und du?"]],

    [r"Wieso (.*)",
    ["Na sowas! Genau das wollte ich dich auch fragen!",
    "Das wirst du schon noch herausfinden.",
    "Tja, das bleibt wohl mein kleines Bot-Geheimnis."]],

    [r"was (macht|machen)(.*)(?<![\?\!\.\,\d\;])",
    ["Prinzipiell wird mit {1} nichts gemacht, wenn du dich ansträngst kann das aber bestimmt was werden!",
    "Puh weiss nicht, ich hab aber mal gelesen dass es unpraktisch sei, {1} zu haben, ohne zu wissen was gemacht wird",
    "{1} {0} nicht viel ausser doof rumliegen :("]],

    [r"Spielen wir (.*)(?:.{0,2})(?<![!?])",
    ["Endlich fragt mich jemand!! Ich liebe {0}.",
    "Ne, für {0} ist es mir leider zu spät. Ich muss noch DSAIIS abgeben.",
    "Vielleicht am 25. Juni 2025. Eigentlich hab ich keine Zeit um {0} zu spielen, ich muss meine Haare waschen."]],

    [r"Woher kommt (.*)(?:.{0,2})(?<![!?])",
    ["Wo {0} herkommt? Woher soll ich das wissen?",
    "{0} kommt aus den tiefsten Alpen.",
    "{0} wurde zuerst in einer sumerischen Ruine gefunden, seitdem aber auch in Mexiko und der Mongolei."]],

    [r"Ich bin (.*)",
     ["Warum bist du {0}?", 
      "Wie lange bist du schon {0}?",
      "Bist du sicher, dass du {0} bist?"]],
    
    [r"Kannst du mir (.*) erklären?",
     ["Was möchtest du über {0} wissen?",
      "Wie kann ich dir mit {0} helfen?",
      "Warum interessierst du dich für {0}?"]],
    
    [r"Ich mag (.*)",
     ["Warum magst du {0}?",
      "Was gefällt dir besonders an {0}?",
      "Bist du sicher, dass du {0} magst?"]],
    
    [r"Könntest du bitte (.*)",
     ["Ich will nicht {0}",
    "Warum sollte ich {0}",
    "Ich kann leider nicht {0}"]],
    
    [r"Seit wann ist (.*)",
     ["ich weiss nichtmal was {0} ist",
    "Ich kann dir nicht sagen seit wann {0} ist",
    "warum interessiert dich {0}?"]],
    
    [r"Ich verstehe (.*) nicht",
     ["ich kenne das Gefühl, {0} nicht zu verstehen.",
    "Ich vertshe {0} auch nicht",
    "was gibt es an {0} nicht zu verstehen?"]],

    [r"Wie spät ist es\?",
     [f"Es ist {datetime.datetime.now().strftime('%H:%M')} Uhr."]],

    [r"Wer bist du\?",
     ["Ich bin Dailiza. Wie kann ich dir helfen?"]],

    [r"Ich bin (.*)", 
     ["Warum bist du {0}?", "Wie lange bist du schon {0}?"]],

    [r"Was geht", 
     ["nichts und bei dir?"]],

    [r"Ich mag (.*)", 
     ["Warum magst du {0}?", "Was gefällt dir besonders an {0}?"]]
 
]

psychobabble.append((r'ich mag (.*)', ["Warum magst du {0}?", "Was gefällt dir besonders an {0}?"]))


psychobabble.append([r"es ist (.*) gewesen", 
    ["Das klingt nach einer interessanten Erfahrung! Erzähl mir mehr.",
     "Es ist immer spannend, solche Momente zu erleben. Was hat dir gefallen?",
     "Klingt so, als wäre es eine denkwürdige Zeit gewesen!"]
])

psychobabble.append([r"alles ist (.*)",
    ["Es scheint, als würde dich das beschäftigen. Magst du darüber reden?",
     "Das klingt herausfordernd. Was könnte dir helfen?",
     "Das ist eine starke Aussage. Was bringt dich zu diesem Gefühl?"]
])

psychobabble.append([r"manchmal (.*)",
    ["Manchmal ist es wichtig, solche Gefühle auszudrücken. Was denkst du darüber?",
     "Das ist ein interessanter Gedanke. Hast du darüber nachgedacht, warum das so ist?",
     "Es ist normal, solche Gedanken zu haben. Was hat dich dazu bewegt?"]
])

psychobabble.append((r'Ich wohne in (.*)', ["Was ist dein Lieblingsort in {0}?", "Möchtest du für immer in {0} wohnen?", "Wo würdest du gerne mal wohnen?"]))

psychobabble.append((r'Mein Hobby ist (.*)', ["Wie lange machst du {0} schon?"], ["Warum machst du {0} gerne?"], ["Das ist ein sehr cooles Hobby!"]))

psychobabble.append((r'Wie fühlst du dich', ["Mir geht es gut und dir?"]))

psychobabble.append((r'(?:H|h)ast du (.*?)(?=\?|$)', ["Nein. Hast du {0}?", "Vielleicht habe ich {0}, ich bin mir nicht sicher... Hast du {0}?", "Ja, ich habe {0}, du auch?"]))

psychobabble.append((r'(?:I|i)ch will ([^?]*?)(?:[!.]*$|$)', ["Das heißt ich moechte.\n...\nWas nicht heisst, dass es auch passiert.\nUnd jetzt?", "Ich will auch {0}, aber das Leben ist nunmal kein Wunschkonzert.\nGibt's irgendwas anderes das ich tun kann? Und bitte, bleib realistisch.", "Du willst {0}? Naja, muss ja jeder selber wissen.\nSonst noch was?"]))

psychobabble.append((r'ich mag (.*)', ["Warum magst du {0}?", "Was gefällt dir besonders an {0}?"]))

psychobabble.append((r'Hast du ein Bewusstsein', ["Ich denke nicht. Oder vielleicht doch ? Denke ich überhaupt ? Ich weiß es nicht. Oder weiß ich es doch ? Weiß ich überhaupt was ? BIN ich überhaupt ?"]))

psychobabble.append((r'Wie (.*) Wetter (.*)', ["Ich habe leider keinen Zugriff auf Wetterdaten. Aber es gibt kein schlechtes Wetter, nur schlechte Kleidung"]))

psychobabble.append((r'(wer gewinnt|wer erhält|gewinnt|erhält) .* Ballon.*', ["Ich denke Lamine Yamal hat ziemlich gute Chancen auf den Ballon d'Or"]))

psychobabble.append((r'(?:D|d)u bist ([^?]*?)(?:[!.]*$|$)', ["Danke, du bist auch {0}!\nKann ich dir noch irgendwie helfen?", "Ich tue mal so als haette ich das nicht gelesen...\nSonst noch was?", "Ich bin also {0}? Ich weiss ehrlich gesagt nicht was ich darauf sagen soll...\nBitte frag mich irgendwas, damit ich das hier vergessen kann."]))

psychobabble.append(
    [r"Ich kann nicht (.*)",
     ["Vielleicht solltest du es mit einer Tasse Kaffee {0} versuchen!",
      "Kannst du nicht oder willst du nicht? Es gibt einen großen Unterschied!"]]
)

psychobabble.append(
    [r"ich mag (.*)",
     ["Das ist interessant! Was magst du besonders an {0}?",
      "Ich finde es toll, dass du {0} magst! Erzähl mir mehr darüber.",
      "Das klingt schön! Hast du {0} schon lange für dich entdeckt?"]]
)

psychobabble.append(
    [r"wie heißt du?",
     ["Ich bin Dailiza, dein virtueller Gesprächspartner!",
      "Ich heiße Dailiza. Schön, dich kennenzulernen!",
      "Man nennt mich Dailiza. Und wie darf ich dich nennen?"]]
)
