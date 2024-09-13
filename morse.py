morse_letter_to_symb_table={
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ".":".-.-.-",
    ",":"..-..",
    "?":"..--..",
    ";":"-.-.-",
    ":":"---...",
    "!":"-.-.--",
    "-":"-....-",
    #" ":"   ",
    " ":"/"
}

morse_sym_to_letter_table={
    ".-":"A",
    "-...":"B",
    "-.-.":"C",
    "-..":"D",
    ".":"E",
    "..-.":"F",
    "--.":"G",
    "....":"H",
    "..":"I",
    ".---":"J",
    "-.-":"K",
    ".-..":"L",
    "--":"M",
    "-.":"N",
    "---":"O",
    ".--.":"P",
    "--.-":"Q",
    ".-.":"R",
    "...":"S",
    "-":"T",
    "..-":"U",
    "...-":"V",
    ".--":"W",
    "-..-":"X",
    "-.--":"Y",
    "--..":"Z",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    "-----":"0",
    ".-.-.-":".",
    "..-..":",",
    "..--..":"?",
    "-.-.-":";",
    "---...":":",
    "-.-.--":"!",
    "-....-":"-",
    "...---...":"SOS",
    "   ":" ",
    "/":" "
}

#message="hello there, here is my truce to everyone in this motherfucking town, where all is and all isnt, I hope ya'll listen to me. We train tonight!. Tonight is the night of reckoning, and in plaintext we will know, and in plain text we will decypher, the thoughts and pleasures of the universe within us, of emtpy seas and dry land, of burning volcanoes and crazy riches, for tonight, we dine in hell. We were born to inherit the stars. Long live the fighters, Lisan al Gaib!"
# message="hey there"
message="Lisan al-gaib! long live the fighters! We were born to inherit the stars. Go to the coordinates, 102.4, 064.3, 123.5, and we shall go to war. Fret not, for the mahdi will be with us, and we shall not grow old. SPill the water of the infidels! The great houses shall know, the holy war has begun! Where is your faith!? Where is the land that brought you here!TO THE STARS, TO THE GREAT HOUSES, BRING THEIR WAR TO THEM. WE SHALL NOT GROW OLD, AND THEY SHALL NOT KNOW, THAT WE ARE THE ONES BORN TO INHERIT THE STARS. AND IN PLAIN TEXT WE WILL KNOW, AND IN PLAIN TEXT WE WILL DECIPHER, THAT WE ARE THE CHILDREN OF THE UNIVERSE FORGOTTEN"
message="The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages. the following message is sent to whoever recieves and understands, It is a short message to all of the order.... SOS, SOS, XOX, START: THIS MESSAGE IS ENCRYPTED IN STANDARD MORSE, STANDARD GREETING, STANDARD KEY. ENCRYPT START: YF3H FHYKSHFJSFLP!,;-?2PFUTY.TF.;AF2M2AI-.7;6Y?Y;Y 5X:.R6DT0NU?Y;; T4UY2G7R7.3!.?CZN:P:0EX6XUZMC05SJ1C7?R7CG47F037:ZJ H!W;6;7 ,H--.USMC7.7.VHF?SZAI?S5D;V VMUP;.L.KIF!G?LNMYO0IS.,.42-4B!1FXZFWV.1NM633?,3V25S?I7FT.?VN?Y;; XT5O1F,QFUTY.PR 2-F?M2AAYFM26YB5AG.:WZT6MDN5V.PSAI,.4VO0,,UC.6SS4CTBFCZ2Y:NIXU;6Y?X4;4 Y2.V.B!,7!?.;;RFMXZ0AQPFNS?I4XU:A.X0S62YUMC34?V YU0X:.:,F5M,HVXPFTPM5GYFXZ;H30DZY35M-M!VX6!.4,-VVA8F?5X:.:,FLG2XK!B,AN?AU!A7R0P60PXEHN.OVFXV;H.3,X-QA:V:5P!P2J.!,JU?.5FASZA T;7W6F20CZV!NAPM?RV;6B4F8TKA4 O-WA.O6I5?W.TR:?N.4 ?3F3PFXV-N4P!AI-M.RWF OM81SF:A U2XMXUFXQ5V.EL4?PDZ320AQGA.6Y.LVZNADZFJV?1I2;20S.A PT?5ORDF-MQ.LTI2OU4 U :ENCRYPT END: MESSAGE END "
encrypt='... --- ...   ...---...   ...---...   ... -- ...    ... - .- .-. - ---... .-- .    .- .-. .    ... .. -. -.- .. -. --.    .-- .   .- .-. .    ... .. -. -.- .. -. --.    -. . . -..    .... . .-.. .--.    ..- .-. --. . -. - .-.. -.--   .-.. --- -.-.     .---- ----- .-.-.- ..... -.    -.... ....- .-.-.- --... .   ---... -- ... --.     . -. -..    ...---...    ...---...    ...---...   --- -. .-.. -.--    .-- .--    -.- -. --- .-- ...   -.-.-.   -.-.  --.- -..   ...---...   .. -.    .-   .--. .-.. .- -.-. .     ..-. ..- .-.. .-..    --- ..-.    ... --- .-. .-. --- .-- ...    .-- .     .-.. .- ..- --. ....     -... . -.-. .- ..- ... .     .. - ...    - .... .    --- -. .-.. -.--    - .... .. -. --.     .-- .    -.-. .- -.    -.. ---    .. -   .. ...    .--. . .-. .... .- .--. ...    - .... .     .. -. .- -... .. .-.. .. - -.--    - ---     .-.. . .- .-. -.'
def morse_encrpytor(message):
    cap_massage=message.upper()
    print(cap_massage)
    print('')
    output=""
    for letter in cap_massage:
        for letter_ in morse_letter_to_symb_table:
            if letter==letter_:
                output+=morse_letter_to_symb_table[letter_]+" "
    print(output)
    return output

def morse_decryptor(message):
    local_message=message
    message_list=[]
    message_word_list=local_message.split('   ')
    for word in message_word_list:
        word_list=word.split(' ')
        for letter in word_list:
            message_list.append(letter)
        message_list.append('   ')
    output=""
    for symb in message_list:
        for letter in morse_sym_to_letter_table:
            if symb==letter:
                output+=morse_sym_to_letter_table[letter]
    print(output)
    return output

morse_encrpytor(message)
morse_decryptor(encrypt)


message2="Ego credidi te et tu me tradis x mors vincit omnia"
message2=message2.upper()
message2=message2.replace(' ','')
print(message2)

morse_encrpytor('SOS SOS SOS TTTT TTTT TTTT BEGIN ENCRYPTED MESSAGE: CIWMHUDMTUVCEJTSOMDHQDMIJOMRIVGPKSJEMRYM  : END ENCRYPTED MESSAGE S0S X mors vincit omnia x layer 2 ')