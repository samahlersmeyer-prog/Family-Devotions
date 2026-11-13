# January 2027: Christmas into Epiphany, then the Small Catechism (Ten Commandments, Creed, Lord's Prayer).
def babe(x,y=196): return f'<ellipse cx="{x}" cy="{y}" rx="24" ry="10"/><circle cx="{x+18}" cy="{y-6}" r="8"/>'
def dove(x,y): return f'<path d="M{x-30},{y} q14,-10 30,-4 q14,-24 34,-22 q-8,14 -18,22 q14,0 22,8 q-22,6 -38,4 q-16,6 -30,-8 Z"/><circle cx="{x-20}" cy="{y-2}" r="1.4" class="dot"/>'
def rays(x,y0,y1,n=5): return ''.join(f'<path d="M{x+k*14},{y0} L{x+k*40},{y1}" fill="none" stroke-width="1.2" stroke-dasharray="4 5"/>' for k in range(-(n//2),n//2+1))
def flames(x,y,h=40): return f'<path d="M{x-10},{y} C{x-14},{y-h*.5} {x},{y-h*.7} {x},{y-h} C{x+2},{y-h*.7} {x+14},{y-h*.5} {x+10},{y} Z"/>'
def furnace(x): return f'<path d="M{x-110},300 V150 Q{x},110 {x+110},150 V300 Z M{x-70},300 V210 Q{x},180 {x+70},210 V300"/>'+''.join(flames(x+dx,300,h) for dx,h in [(-50,70),(-20,90),(10,80),(40,70)])
def cart(x): return f'<path d="M{x-80},250 H{x+60} V210 H{x-60} Z M{x+60},250 L{x+110},236"/><circle cx="{x-40}" cy="270" r="26"/><circle cx="{x-40}" cy="270" r="4" class="dot"/><circle cx="{x+30}" cy="270" r="26"/><circle cx="{x+30}" cy="270" r="4" class="dot"/>'
def seed(x,y): return f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3" class="dot"/>'
def bird(x,y): return f'<path d="M{x-14},{y} q7,-8 14,0 q7,-8 14,0" fill="none"/>'
def flower(x,h=60): return f'<path d="M{x},300 V{300-h}" fill="none"/>'+''.join(f'<ellipse cx="{x+dx}" cy="{300-h+dy}" rx="7" ry="7"/>' for dx,dy in [(-9,0),(9,0),(0,-9),(0,9)])+f'<circle cx="{x}" cy="{300-h}" r="5"/>'
def vines(x0,x1): return ''.join(f'<path d="M{x},300 V240 M{x-16},250 H{x+16}" fill="none"/>'+''.join(f'<circle cx="{x+dx}" cy="{256+dy}" r="4"/>' for dx,dy in [(-10,0),(-6,6),(-2,0),(8,2),(4,8)]) for x in range(x0,x1,44))
def rock(x): return f'<path d="M{x-80},300 Q{x-70},240 {x-10},236 Q{x+60},232 {x+80},300 Z"/>'
def loaves(x): return ''.join(f'<ellipse cx="{x+i*26}" cy="292" rx="14" ry="8"/>' for i in range(5))+fish(x+150,284)+fish(x+150,298)

S="Christmas"
D("2027-01-01","New Year’s Day","The Name of Jesus","Mom or Dad","Luke 2:21",[(21,"And at the end of eight days, when he was circumcised, he was called Jesus, the name given by the angel before he was conceived in the womb.")],
"Eight days old",[
"Happy New Year! On the first day of the year, the church remembers something that happened when Jesus was just eight days old. On that day, baby boys in Israel were brought into God’s covenant family, a little like how babies are baptized today. And on that day, the baby was given His name.",
"Mary and Joseph didn’t have to think up a name or look through a list. The angel Gabriel had already told them: “You shall call His name Jesus.” So on the eighth day, they named Him Jesus, just as God had said.",
"“Jesus” means “The Lord saves.” It’s the name above every name. The Bible says that one day every knee will bow at the name of Jesus. Christians have always started new things in Jesus’ name, and that’s a good way to start a new year too."],
"In Jesus’ name",["We begin every devotion “In the name of the Father and of the Son and of the Holy Spirit,” the same name God put on you in your Baptism. Whatever this year brings, you belong to Him. You can start every day, and every prayer, in Jesus’ name."],
["How old was Jesus when He was named? Who chose His name?","What does the name Jesus mean?","What does it mean to do something “in Jesus’ name”? How could our family start this year in His name?"],
"Lord Jesus, Your name is above every name. Thank You for saving us, and for putting Your name on us in Baptism.","Bless our family in this new year, and help us do everything in Your name.",
"When Jesus was eight days old, Mary and Joseph named Him Jesus, just as the angel said!",
["Jesus was named when He was [eight] days old.","The [angel] told Mary His name.","Jesus means “The Lord [saves].”","Every [knee] will bow at His name.","God put His name on us in [Baptism]."],
["JESUS","NAME","EIGHT","SAVES","ANGEL","NEWYEAR"],[("Who chose Jesus’ name?",["God, through the angel","Mary’s friends"],0),("What does Jesus mean?",["The Lord saves","Little lamb"],0)],
"Write JESUS in big letters and decorate it for the new year.",("Luke 2:21","“He was called Jesus, the name given by the angel.”"),
scene(sun(560,60),temple(),person(250,beard=False,arms="open",hair="wrap"),babe(250),person(400,beard=True,arms="open",hair="short"),label="Coloring picture: Mary and Joseph with baby Jesus at the temple"))

D("2027-01-02",S,"Out of Egypt","a 3rd–5th grader","Matthew 2:14–15",[(14,"And he rose and took the child and his mother by night and departed to Egypt"),(15,"and remained there until the death of Herod. This was to fulfill what the Lord had spoken by the prophet, “Out of Egypt I called my son.”")],
"Coming home",[
"Remember how an angel warned Joseph to take Mary and baby Jesus to Egypt to escape wicked King Herod? They stayed in Egypt until Herod died. Then an angel came to Joseph in a dream once more: “Get up, take the child and His mother, and go back to the land of Israel.”",
"So Joseph packed up his little family and made the long trip home. They settled in the small town of Nazareth, in Galilee. That’s why people would later call Jesus “Jesus of Nazareth.”",
"Matthew noticed something amazing. Long ago, God had brought His people Israel out of Egypt in the exodus, through the Red Sea. And the prophet Hosea had written, “Out of Egypt I called My son.” Now God was calling His Son Jesus out of Egypt too. Jesus was walking the same road as God’s people, to rescue them for good."],
"Jesus walks our road",["Jesus went where His people went: to Egypt and back, through hard times and long trips. Jesus knows what it’s like to move, to be afraid, and to start over somewhere new. Wherever our family goes, He has gone before us."],
["Where did Jesus’ family live while Herod was alive? Which town did they move to?","How many times did an angel speak to Joseph in a dream? Can you remember them?","Israel came out of Egypt, and so did Jesus. Why do you think Matthew wanted us to notice that?"],
"Lord Jesus, thank You for walking the same road as Your people, and for keeping Your family safe. Thank You for Joseph, who listened and obeyed every time.","Go with our family wherever we go this year.",
"An angel told Joseph to bring Jesus home from Egypt. They moved to Nazareth!",
["Jesus’ family stayed in [Egypt] until Herod died.","An angel spoke to Joseph in a [dream].","They moved to the town of [Nazareth].","“Out of Egypt I called My [son].”","Joseph always [obeyed] God."],
["EGYPT","NAZARETH","DREAM","JOSEPH","HOME","SON"],[("Where did Jesus grow up?",["Nazareth","Rome"],0),("Did Joseph listen to the angel?",["Yes","No"],0)],
"Draw Mary, Joseph, and Jesus traveling home from Egypt.",("Matthew 2:15","“Out of Egypt I called my son.”"),
scene(sun(560,56),pyramids(),donkey(250),person(130,beard=True,arms="mixed",hair="wrap",s=.85),'<g transform="translate(0,-72)">'+person(250,beard=False,arms="open",hair="wrap",s=.55)+'</g>',label="Coloring picture: Jesus’ family traveling home from Egypt"))

D("2027-01-03",S,"In My Father’s House","an older kid","Luke 2:49",[(49,"And he said to them, “Why were you looking for me? Did you not know that I must be in my Father’s house?”")],
"The boy Jesus in the temple",[
"Every year, Jesus’ family walked to Jerusalem for the Passover feast. When Jesus was twelve, they went as usual. Lots of relatives and neighbors traveled together in a big group. After the feast, Mary and Joseph started home, thinking Jesus was somewhere in the crowd with friends.",
"After a whole day of walking, they looked for Him, and He wasn’t there! They hurried back to Jerusalem and searched for three days. Imagine how worried they were! Finally they found Him in the temple, sitting with the teachers, listening and asking questions. Everyone was amazed at how much He understood.",
"Mary said, “Son, why did You do this? We’ve been looking for You everywhere!” Jesus answered, “Why were you looking for Me? Didn’t you know I must be in My Father’s house?” Then He went home to Nazareth with them and obeyed them."],
"His Father’s house",["Even at twelve, Jesus knew who His real Father was: God! And He loved being where God’s Word was taught. Church is our Father’s house too. When we gather to hear God’s Word, we’re right where Jesus loved to be."],
["How old was Jesus? Where did Mary and Joseph find Him?","How many days did they search? How do you think they felt?","Jesus called the temple “My Father’s house.” What was He telling Mary and Joseph about who He is?"],
"Heavenly Father, thank You for Jesus, who loved Your house and Your Word. Thank You for our church, where we hear You speak.","Give us hearts that love to be in Your house and to learn Your Word.",
"When Jesus was twelve, Mary and Joseph found Him in the temple. He said, “I must be in My Father’s house!”",
["Jesus was [twelve] years old.","They went to Jerusalem for the [Passover].","Mary and Joseph searched for [three] days.","They found Him in the [temple].","Jesus said, “I must be in My [Father]’s house.”"],
["TEMPLE","TWELVE","TEACHERS","FATHER","SEARCH","PASSOVER"],[("Where was Jesus?",["In the temple","At the market"],0),("Who is Jesus’ true Father?",["God","Joseph"],0)],
"Draw young Jesus in the temple with the teachers.",("Luke 2:49","“Did you not know that I must be in my Father’s house?”"),
scene(temple(),person(320,beard=False,arms="open",hair="curly",s=.7),person(190,beard=True,arms="mixed",hair="wrap",s=.9),person(450,beard=True,arms="open",hair="wrap",s=.9),scroll(320,256),label="Coloring picture: young Jesus with the teachers in the temple"))

D("2027-01-04",S,"Jesus Grew","a K–2nd grader, with help","Luke 2:51–52",[(51,"And he went down with them and came to Nazareth and was submissive to them. And his mother treasured up all these things in her heart."),(52,"And Jesus increased in wisdom and in stature and in favor with God and man.")],
"Growing up in Nazareth",[
"After the trip to the temple, Jesus went home to Nazareth with Mary and Joseph. The Bible tells us almost nothing about the next eighteen years! But it tells us something important: Jesus obeyed His parents.",
"Jesus grew up in a regular town, in a regular home. Joseph was a carpenter, so Jesus probably learned to work with wood and tools. Later He had younger brothers and sisters. He did chores, ate meals with His family, and went to the synagogue on the Sabbath to hear God’s Word.",
"Luke says Jesus grew in wisdom, and in stature, which means He got taller, and in favor with God and with people. The Son of God was once a kid, then a teenager. He knows what it’s like to grow up."],
"Obeying for us",["Jesus obeyed His parents perfectly. He never talked back, never rolled His eyes, and never ignored them. Why does that matter? Because He did it for us. Where we fail, Jesus kept God’s law in our place, and He forgives us when we don’t obey."],
["What town did Jesus grow up in? What was Joseph’s job?","What four ways did Jesus grow?","Jesus obeyed His parents perfectly, for us. How does that help us when we don’t obey?"],
"Lord Jesus, thank You for growing up as one of us, and for obeying perfectly in our place. Forgive us for the times we don’t listen.","Help us grow in wisdom and in love for You, and help us honor our parents.",
"Jesus grew up in Nazareth. He obeyed His parents and grew in wisdom and stature!",
["Jesus grew up in [Nazareth].","Joseph was a [carpenter].","Jesus [obeyed] His parents.","He grew in [wisdom].","Stature means He got [taller]."],
["NAZARETH","WISDOM","GROW","TOOLS","OBEY","FAMILY"],[("Did Jesus obey His parents?",["Yes","No"],0),("Was Jesus ever a kid?",["Yes","No"],0)],
"Draw Jesus helping Joseph in the carpenter shop.",("Luke 2:52","“Jesus increased in wisdom and in stature.”"),
scene(sun(560,56),house(470),person(170,beard=True,arms="mixed",hair="short"),person(290,beard=False,arms="open",hair="curly",s=.6),'<path d="M80,280 h120 v12 h-120 Z M210,286 l40,-20 l6,8 l-40,20 Z"/>',label="Coloring picture: Jesus growing up with Joseph the carpenter"))

D("2027-01-05",S,"A Star Out of Jacob","an older kid","Numbers 24:17",[(17,"I see him, but not now; I behold him, but not near: a star shall come out of Jacob, and a scepter shall rise out of Israel…")],
"Balaam and the talking donkey",[
"Long before Jesus, when Israel was traveling through the desert, an enemy king named Balak was afraid of them. He hired a man named Balaam to put a curse on Israel. Balaam saddled his donkey and set out. But God sent an angel with a sword to stand in the road.",
"Balaam couldn’t see the angel, but his donkey could! The donkey turned off the road, then squeezed against a wall and crushed Balaam’s foot, then lay right down. Balaam got angry and hit her. Then God opened the donkey’s mouth, and she talked! “What have I done to you, that you hit me three times?” Then God opened Balaam’s eyes, and he saw the angel too.",
"When Balaam finally opened his mouth to curse Israel, only blessings came out! And God gave him an amazing prophecy: “A star shall come out of Jacob, and a scepter shall rise out of Israel.” A scepter is a king’s staff. Many think the wise men from the East knew this promise and watched for a King’s star."],
"Nobody can curse God’s people",["The king wanted a curse, but God turned it into a blessing. Even a donkey and a hired prophet couldn’t stop God’s plan. Jesus is the Star out of Jacob, and tomorrow is Epiphany, when we celebrate the wise men finding Him."],
["What animal talked? What did it see in the road?","What happened every time Balaam tried to curse Israel?","Balaam saw the King “not now… not near.” How did his prophecy come true?"],
"Lord God, thank You that no one can curse the people You have blessed. Thank You for Jesus, the Star out of Jacob and our King.","Open our eyes to see You at work, like You opened Balaam’s eyes.",
"Balaam’s donkey saw an angel and talked! Then Balaam promised a star would come out of Jacob.",
["A king wanted Balaam to [curse] Israel.","Balaam’s [donkey] saw the angel.","God made the donkey [talk].","Balaam could only say [blessings].","“A [star] shall come out of Jacob.”"],
["BALAAM","DONKEY","ANGEL","STAR","SCEPTER","BLESSING"],[("Who saw the angel first?",["The donkey","Balaam"],0),("Did Balaam curse Israel?",["Yes","No"],1)],
"Draw Balaam’s donkey talking, with the angel in the road.",("Numbers 24:17","“A star shall come out of Jacob.”"),
scene(star(120,60,18),donkey(260),'<g transform="translate(0,-60)">'+person(255,beard=True,arms="open",hair="wrap",s=.6)+'</g>',angel(500,.75),label="Coloring picture: Balaam’s donkey seeing the angel in the road"))

S="Epiphany"
D("2027-01-06","Epiphany","The Wise Men Worship","Mom or Dad","Matthew 2:10–11",[(10,"When they saw the star, they rejoiced exceedingly with great joy."),(11,"And going into the house, they saw the child with Mary his mother, and they fell down and worshiped him. Then, opening their treasures, they offered him gifts, gold and frankincense and myrrh.")],
"Following the star",[
"Today is Epiphany! Christmas lasts twelve days, and tonight it ends with the visit of the wise men. They came from far away in the East, maybe from Persia or Babylon. They studied the stars, and when they saw a new star rise, they believed a great King had been born.",
"They traveled for weeks or even months to find Him. In Jerusalem, King Herod sent them to Bethlehem, just as Micah had promised. And the star went ahead of them until it stopped over the place where Jesus was. They were filled with joy!",
"Inside the house, they saw the child with Mary His mother, and they bowed down and worshiped Him. They opened their treasures: gold, a gift for a king; frankincense, incense for worshiping God; and myrrh, a spice used when someone died. Their gifts told who Jesus is: King, God, and the Savior who would die for us."],
"Jesus for the nations",["“Epiphany” means “showing.” The wise men weren’t from Israel. They were outsiders, and God showed them His Son. That means Jesus came for every nation, including us. The Epiphany season is about Jesus being shown to the whole world."],
["What led the wise men to Jesus? What three gifts did they bring?","What does each gift tell us about Jesus?","The wise men weren’t Jewish. Why is it good news for us that God showed Jesus to them?"],
"Lord Jesus, King of kings, thank You for leading the wise men to You, and for showing Yourself to the whole world, even to us.","Like the wise men, help us worship You and give You our very best.",
"The wise men followed the star to Jesus and gave Him gold, frankincense, and myrrh!",
["The wise men followed a [star].","They came from the [East].","They [worshiped] Jesus.","Gold was a gift for a [king].","Epiphany means “[showing].”"],
["EPIPHANY","STAR","GOLD","MYRRH","WORSHIP","KING"],[("What does Epiphany mean?",["Showing","Sleeping"],0),("Is Jesus for every nation?",["Yes","No"],0)],
"Draw the wise men kneeling with their gifts.",("Matthew 2:11","“They fell down and worshiped him.”"),
scene(bigstar(470,46),person(500,beard=False,arms="open",hair="wrap",s=.85),babe(500,216),person(130,beard=True,arms="open",hair="wrap",s=.75),person(230,beard=True,arms="mixed",hair="short",s=.75),person(330,beard=False,arms="open",hair="curly",s=.75),crown(130,166),crown(230,166),crown(330,166),gift(600),label="Coloring picture: the wise men worshiping Jesus"))

D("2027-01-07",S,"Arise, Shine","a 3rd–5th grader","Isaiah 60:1, 3",[(1,"Arise, shine, for your light has come, and the glory of the LORD has risen upon you."),(3,"And nations shall come to your light, and kings to the brightness of your rising.")],
"Light for the nations",[
"Long ago, Isaiah promised that the light of the Lord would rise, and nations and kings would come to it. The wise men were the first ones from far away to come to Jesus. But they wouldn’t be the last! After Jesus rose and went back to heaven, His followers carried the good news to every land.",
"About 1,300 years ago, the people of Germany still worshiped false gods. A missionary named Boniface traveled there to tell them about Jesus. An old story says the people worshiped a giant oak tree they believed belonged to the thunder god Thor. Boniface took an axe and chopped it down! When nothing bad happened to him, many people believed in the true God.",
"Another old story says a little evergreen tree was growing nearby, and Boniface said it pointed up to heaven, green all winter like God’s never-ending love. Whether or not that part happened, the gospel truly came to the people of Germany, the land where Martin Luther would be born many years later."],
"The light reaches us",["The good news traveled from Bethlehem to the wise men, then across the world, from person to person, all the way to our family. Someone brought Jesus’ light to your great-great-grandparents. Now it’s our turn to shine it."],
["Who came to Jesus’ light first? Where did Boniface go?","What did Boniface chop down? Why?","Isaiah said nations would come to the light. How did the light of Jesus reach our family?"],
"Lord Jesus, You are the light of the nations. Thank You for every missionary who carried Your good news, and for bringing Your light to our family.","Help us shine Your light to our friends and neighbors.",
"Isaiah said, “Arise, shine, for your light has come!” Missionaries carried Jesus’ light to the whole world.",
["“Arise, [shine], for your light has come.”","[Nations] shall come to your light.","Boniface was a [missionary].","He chopped down an [oak] tree.","Now it’s our turn to [shine]."],
["ARISE","SHINE","NATIONS","BONIFACE","OAK","LIGHT"],[("Did Thor stop Boniface?",["Yes","No"],1),("Who is the light of the nations?",["Jesus","Thor"],0)],
"Draw a big evergreen tree pointing up to heaven.",("Isaiah 60:1","“Arise, shine, for your light has come.”"),
scene(sun(560,60),'<path d="M320,300 V270 M260,270 L320,90 L380,270 Z M276,220 H364 M290,170 H350"/>','<path d="M110,300 h70 v-26 h-70 Z"/>','<path d="M480,300 L520,230 M512,220 l22,10 l-6,14 l-22,-10 Z"/>',person(450,beard=True,arms="mixed",hair="short",s=.8),label="Coloring picture: an evergreen tree and a stump"))

D("2027-01-08",S,"Naaman Washes in the Jordan","a K–2nd grader, with help","2 Kings 5:14",[(14,"So he went down and dipped himself seven times in the Jordan, according to the word of the man of God, and his flesh was restored like the flesh of a little child, and he was clean.")],
"A little girl’s big faith",[
"Naaman was a great army general in the land of Aram, but he had a terrible skin disease called leprosy. In his house lived a little servant girl who had been taken from Israel. She could have been angry. Instead she told Naaman’s wife, “I wish my master would go see the prophet in Israel. He would heal him!”",
"So Naaman went with his horses and chariots to the house of the prophet Elisha. Elisha didn’t even come out. He just sent a message: “Go wash in the Jordan River seven times, and you will be clean.” Naaman was furious! “That’s it? Our rivers at home are better than this muddy Jordan!”",
"But his servants said, “If the prophet asked you to do something hard, you would do it. Why not just wash?” So Naaman went down to the Jordan and dipped himself seven times. When he came up, his skin was as smooth as a little child’s! Naaman said, “Now I know there is no God in all the earth but in Israel.”"],
"Water and God’s Word",["The Jordan wasn’t magic water. What healed Naaman was God’s promise connected to the water. That’s what Baptism is like. It looks like plain water, but God’s Word is with it, and it washes away our sin. And it all started with a little girl who told about the true God."],
["Who told Naaman about the prophet? What did Elisha tell him to do?","Why was Naaman angry at first?","What made the water able to heal Naaman? How is Baptism like that?"],
"Lord God, thank You for the little girl who told Naaman about You, and for healing him. Thank You for washing us clean in Baptism.","Give us faith like that little girl, to tell others about You.",
"Naaman washed in the Jordan River seven times, and God made him clean! A little girl told him where to go.",
["Naaman had a skin disease called [leprosy].","A little servant [girl] told about the prophet.","The prophet’s name was [Elisha].","Naaman washed in the [Jordan] River.","He dipped himself [seven] times."],
["NAAMAN","JORDAN","ELISHA","SEVEN","CLEAN","GIRL"],[("Who told Naaman about God’s prophet?",["A little girl","The king"],0),("How many times did he wash?",["Seven","Two"],0)],
"Draw Naaman coming up out of the Jordan River, clean!",("2 Kings 5:14","“He went down and dipped himself seven times in the Jordan.”"),
scene(sun(560,56),hills(),waves(282),person(320,beard=True,arms="up",hair="short",s=.8),person(140,beard=False,arms="open",hair="curly",s=.55),label="Coloring picture: Naaman washing in the Jordan River"))

D("2027-01-09",S,"Philip and the Traveler","a 3rd–5th grader","Acts 8:35",[(35,"Then Philip opened his mouth, and beginning with this Scripture he told him the good news about Jesus.")],
"Here is water!",[
"After Jesus went back to heaven, an angel told a disciple named Philip, “Go south to the desert road.” Philip didn’t know why, but he went. On the road came a chariot carrying an important official from Ethiopia, in Africa. He was the treasurer for the queen, and he was reading from the prophet Isaiah.",
"The Holy Spirit told Philip, “Go up to that chariot.” Philip ran alongside and heard the man reading out loud. “Do you understand what you’re reading?” “How can I, unless someone explains it to me?” The man was reading Isaiah 53, about a lamb led to the slaughter. So Philip climbed in and told him the good news about Jesus, the Lamb of God.",
"As they rode along, they came to some water. The man said, “Look, here is water! What prevents me from being baptized?” They stopped the chariot, went down into the water, and Philip baptized him. Then the man went on his way rejoicing, carrying the good news back to Africa."],
"Baptism brings joy",["The man from Ethiopia heard about Jesus and wanted to be baptized right away. In Baptism God gave him forgiveness and made him His child. That’s why he went home rejoicing. Your Baptism is a reason to rejoice too."],
["Where was the man from? What was he reading?","How did Philip know to go to that road?","Why did the man go home rejoicing? Do you know the day you were baptized?"],
"Holy Spirit, thank You for sending Philip to explain Your Word, and for bringing the good news to Africa and to us. Thank You for our Baptism.","Use us to explain Your Word to someone who has questions.",
"Philip explained God’s Word to a man from Ethiopia and baptized him. He went home rejoicing!",
["Philip went to the desert [road].","The man was from [Ethiopia].","He was reading the prophet [Isaiah].","Philip told him the good news about [Jesus].","The man was [baptized] and went home rejoicing."],
["PHILIP","CHARIOT","ETHIOPIA","ISAIAH","WATER","REJOICE"],[("What was the man reading?",["Isaiah","A map"],0),("How did he feel after his Baptism?",["Rejoicing","Grumpy"],0)],
"Draw Philip running beside the chariot.",("Acts 8:35","“He told him the good news about Jesus.”"),
scene(sun(560,56),waves(290,420,636),'<g transform="translate(0,-52)">'+person(240,beard=True,arms="open",hair="wrap",s=.55)+'</g>',cart(260),person(440,beard=True,arms="mixed",hair="short",s=.8),label="Coloring picture: Philip and the traveler in the chariot"))

D("2027-01-10","Baptism of Our Lord","Jesus Is Baptized","Mom or Dad","Matthew 3:16–17",[(16,"And when Jesus was baptized, immediately he went up from the water, and behold, the heavens were opened to him, and he saw the Spirit of God descending like a dove and coming to rest on him;"),(17,"and behold, a voice from heaven said, “This is my beloved Son, with whom I am well pleased.”")],
"At the Jordan",[
"Today the church celebrates the Baptism of Jesus. Jesus was about thirty years old. He walked from Nazareth to the Jordan River, where John the Baptist was baptizing people who were sorry for their sins.",
"When John saw Jesus, he said, “I need to be baptized by You! Why are You coming to me?” Jesus had no sins to wash away. But Jesus said, “Let it be so now, to fulfill all righteousness.” Jesus was stepping into our place, standing with sinners, to take our sins on Himself.",
"As Jesus came up out of the water, heaven opened. The Holy Spirit came down on Him like a dove. And the Father’s voice spoke from heaven: “This is My beloved Son, with whom I am well pleased.” The Father, the Son, and the Holy Spirit, all three, were there together."],
"Your Baptism",["When Jesus was baptized, He took our sins. When you were baptized, He gave you His righteousness. And God says to you what He said to Jesus: “You are My beloved child.” Martin Luther, when he was discouraged, used to remind himself, “I am baptized!”"],
["Who baptized Jesus? What came down like a dove?","What did the voice from heaven say?","Jesus didn’t have sins to wash away. Why was He baptized? What does God say to you in your Baptism?"],
"Heavenly Father, thank You for Jesus, Your beloved Son, who stood in our place. Thank You for the Holy Spirit, and for making us Your children in Baptism.","When we feel discouraged, remind us: “I am baptized!”",
"Jesus was baptized in the Jordan. The Spirit came like a dove, and the Father said, “This is My beloved Son!”",
["Jesus was baptized in the [Jordan] River.","[John] baptized Him.","The Spirit came down like a [dove].","The Father said, “This is My beloved [Son].”","Luther said, “I am [baptized]!”"],
["BAPTISM","JORDAN","DOVE","SPIRIT","FATHER","BELOVED"],[("What came down on Jesus like a dove?",["The Holy Spirit","An angel"],0),("Were the Father, Son, and Spirit all there?",["Yes","No"],0)],
"Draw Jesus in the river, with the dove coming down from heaven.",("Matthew 3:17","“This is my beloved Son, with whom I am well pleased.”"),
scene(rays(320,20,110),dove(320,80),hills(),waves(286),person(260,beard=True,arms="open",hair="short",s=.85),person(400,beard=True,arms="mixed",hair="curly",s=.85),label="Coloring picture: Jesus being baptized, with the dove coming down"))
ALL[-1]['cat']=dict(part="Baptism",text="What does Baptism give or profit?",mean="It works forgiveness of sins, delivers from death and the devil, and gives eternal salvation to all who believe this, as the words and promises of God declare.")

S="Small Catechism: The Ten Commandments"
D("2027-01-11",S,"No Other Gods","an older kid","Daniel 3:17–18",[(17,"If this be so, our God whom we serve is able to deliver us from the burning fiery furnace, and he will deliver us out of your hand, O king."),(18,"But if not, be it known to you, O king, that we will not serve your gods or worship the golden image that you have set up.”")],
"The fiery furnace",[
"Tonight we start learning the Small Catechism, the little book Martin Luther wrote for families to learn at home. First come the Ten Commandments. The First Commandment is the most important: “You shall have no other gods.”",
"King Nebuchadnezzar built a gold statue ninety feet tall and ordered everyone to bow down to it when the music played. Anyone who refused would be thrown into a blazing furnace. The music played, and everyone bowed, except three young men from Israel: Shadrach, Meshach, and Abednego. They said, “Our God can save us. But even if He doesn’t, we will not worship your statue.”",
"The furious king made the furnace seven times hotter and threw them in. Then he jumped up. “Didn’t we throw three men in? I see four, walking around in the fire, and the fourth looks like a son of the gods!” When they came out, not a hair was burned, and they didn’t even smell like smoke. God was with them in the fire."],
"Fear, love, and trust",["A god is whatever we trust most and love most. Today most people don’t bow to statues, but we can make a god out of money, sports, screens, or what other people think. The First Commandment calls us to put God first. And when we fail, Jesus, the one who walked in the fire with His people, forgives us."],
["What did the king want everyone to do? What did the three friends do?","How many men did the king see in the fire?","What “gods” are tempting for kids today? What does it mean to fear, love, and trust God above all things?"],
"Lord God, You alone are God. Thank You for being with Your people even in the fire. Forgive us for the times we put other things first.","Help us fear, love, and trust You above all things.",
"Shadrach, Meshach, and Abednego wouldn’t bow to the gold statue. God was with them in the fiery furnace!",
["The king built a [gold] statue.","Three friends would not [bow] to it.","The king threw them into a [furnace].","He saw [four] men walking in the fire.","You shall have no other [gods]."],
["FURNACE","SHADRACH","MESHACH","ABEDNEGO","STATUE","FIRE"],[("Did the three friends bow?",["Yes","No"],1),("Who was with them in the fire?",["God","Nobody"],0)],
"Draw four men walking safely in the fiery furnace.",("Exodus 20:3","“You shall have no other gods before me.”"),
scene(furnace(320),person(240,beard=False,arms="up",hair="short",s=.45),person(300,beard=False,arms="up",hair="curly",s=.45),person(350,beard=False,arms="up",hair="short",s=.45),person(400,beard=False,arms="open",hair="wrap",s=.45),label="Coloring picture: four men walking in the fiery furnace"))
ALL[-1]['cat']=dict(part="The First Commandment",text="Thou shalt have no other gods.",mean="We should fear, love, and trust in God above all things.")

D("2027-01-12",S,"Calling on His Name","a 3rd–5th grader","Matthew 14:30–31",[(30,"But when he saw the wind, he was afraid, and beginning to sink he cried out, “Lord, save me.”"),(31,"Jesus immediately reached out his hand and took hold of him, saying to him, “O you of little faith, why did you doubt?”")],
"Peter on the water",[
"The Second Commandment is “You shall not misuse the name of the Lord your God.” God’s name isn’t just a word. It’s how He gives Himself to us so we can call on Him. So we shouldn’t use it to curse, to swear, to lie, or as a careless exclamation like “OMG.” Instead, we use it to pray, praise, and give thanks.",
"One night the disciples were in a boat in a storm. Before dawn, they saw Jesus walking toward them on the water! Peter said, “Lord, if it’s You, tell me to come to You.” Jesus said, “Come.” Peter climbed out and walked on the water toward Jesus!",
"But then Peter looked at the wind and the waves, and he got scared and began to sink. He cried out, “Lord, save me!” Right away Jesus reached out and caught him. Peter used the Lord’s name exactly the right way: he called on Him in trouble."],
"In every trouble",["Luther says we should “call upon it in every trouble, pray, praise, and give thanks.” God gave us His name so we could cry out to Him like Peter. You can always say, “Lord, help me!” and He hears you."],
["Where was Peter walking? What did he shout when he started to sink?","What are some wrong ways people use God’s name? What are right ways?","Why does God care how we use His name? How did Peter use it the right way?"],
"Lord Jesus, thank You for catching Peter when he called on You, and for hearing us when we call. Forgive us for using Your name carelessly.","Help us use Your name to pray, praise, and give thanks.",
"Peter started to sink and cried out, “Lord, save me!” Jesus caught him. We call on God’s name in every trouble!",
["Peter walked on the [water].","He got scared of the [wind].","He cried, “Lord, [save] me!”","Jesus reached out His [hand].","We call on God’s name to [pray], praise, and give thanks."],
["PETER","WATER","WIND","NAME","PRAY","PRAISE"],[("What did Peter shout?",["Lord, save me!","Leave me alone!"],0),("Can we call on God’s name in trouble?",["Yes","No"],0)],
"Draw Jesus catching Peter on the waves.",("Matthew 14:30","“Lord, save me.”"),
scene(moon(560,56),waves(270),boat(520,232),person(240,beard=True,arms="open",hair="short",s=.8),person(360,beard=True,arms="up",hair="curly",s=.7),label="Coloring picture: Jesus reaching out to Peter on the water"))
ALL[-1]['cat']=dict(part="The Second Commandment",text="Thou shalt not take the name of the Lord thy God in vain.",mean="We should fear and love God that we may not curse, swear, use witchcraft, lie, or deceive by His name, but call upon it in every trouble, pray, praise, and give thanks.")

D("2027-01-13",S,"Sitting at Jesus’ Feet","a K–2nd grader, with help","Luke 10:39",[(39,"And she had a sister called Mary, who sat at the Lord’s feet and listened to his teaching.")],
"Mary and Martha",[
"The Third Commandment is “Remember the Sabbath day by keeping it holy.” God gave Israel a day of rest each week to stop working and hear His Word. For Christians, the most important part is this: we should gladly hear and learn God’s Word, especially when we gather at church.",
"One day Jesus visited the home of two sisters, Martha and Mary. Martha rushed around the kitchen, cooking and cleaning and getting everything ready. Mary sat on the floor at Jesus’ feet, listening to Him teach.",
"Martha got upset. “Lord, don’t You care that my sister left me to do all the work? Tell her to help me!” Jesus answered kindly, “Martha, Martha, you are worried about many things. But only one thing is needed. Mary has chosen the good part, and it won’t be taken away from her.”"],
"The one thing needed",["Life gets busy, like Martha’s kitchen. But the best thing we can do is sit at Jesus’ feet and hear His Word. That’s what we’re doing right now at devotions, and that’s what we do at church. It isn’t a chore. It’s a gift."],
["What was Martha doing? What was Mary doing?","What did Jesus say Mary chose?","Luther says we should “gladly hear and learn” God’s Word. What helps you listen at church?"],
"Lord Jesus, thank You for teaching us Your Word, the one thing we need. Forgive us when we are too busy for You.","Help us gladly hear and learn Your Word at church and at home.",
"Mary sat at Jesus’ feet and listened. Jesus said she chose the good part!",
["The sisters were Mary and [Martha].","Martha was busy in the [kitchen].","Mary sat at Jesus’ [feet].","Mary [listened] to Jesus teach.","We gladly hear and learn God’s [Word]."],
["MARY","MARTHA","LISTEN","SABBATH","WORD","CHURCH"],[("Who listened at Jesus’ feet?",["Mary","Martha"],0),("Is hearing God’s Word a gift?",["Yes","No"],0)],
"Draw Mary sitting at Jesus’ feet.",("Luke 10:39","“Mary, who sat at the Lord’s feet and listened to his teaching.”"),
scene(window(70),person(380,beard=True,arms="open",hair="short"),person(300,beard=False,arms="open",hair="wrap",s=.55),person(540,beard=False,arms="mixed",hair="wrap",s=.85),table(470,620),label="Coloring picture: Mary listening at Jesus’ feet"))
ALL[-1]['cat']=dict(part="The Third Commandment",text="Remember the Sabbath day, to keep it holy.",mean="We should fear and love God that we may not despise preaching and His Word, but hold it sacred, and gladly hear and learn it.")

D("2027-01-14",S,"Where You Go, I Will Go","an older kid","Ruth 1:16",[(16,"But Ruth said, “Do not urge me to leave you or to return from following you. For where you go I will go, and where you lodge I will lodge. Your people shall be my people, and your God my God.")],
"Ruth and Naomi",[
"The Fourth Commandment is “Honor your father and your mother.” It’s the first commandment with a promise: “that it may go well with you.” God gives us parents and others in authority to care for us, and He wants us to honor, serve, obey, love, and cherish them.",
"Naomi was an Israelite woman living in the land of Moab. Her husband died, and then both of her sons died too. Naomi was old and alone, and she decided to go back home to Bethlehem. She told her two daughters-in-law, “Go back to your own families.” One of them, Orpah, kissed her goodbye and left.",
"But the other, Ruth, held on to her. “Don’t ask me to leave you. Where you go, I will go. Your people will be my people, and your God my God.” So Ruth went to Bethlehem and worked hard in the fields to gather grain for Naomi. God blessed Ruth. She married a kind man named Boaz, and she became the great-grandmother of King David!"],
"Honor and care",["Ruth honored Naomi by staying with her and taking care of her. Honoring parents means more than doing what you’re told. It means loving them, helping them, and someday caring for them when they’re old. And Jesus, who came from Ruth’s family, honored His parents perfectly for us."],
["Who stayed with Naomi? Where did they go?","How did Ruth take care of Naomi?","Ruth honored Naomi even when it was hard. What are ways kids can honor parents, grandparents, and teachers?"],
"Heavenly Father, thank You for parents, grandparents, and everyone who cares for us. Thank You for Ruth’s loyal love.","Help us honor, serve, obey, love, and cherish the people You put over us.",
"Ruth told Naomi, “Where you go, I will go.” She took care of Naomi and became King David’s great-grandmother!",
["Ruth stayed with [Naomi].","They went to [Bethlehem].","Ruth gathered [grain] in the fields.","She married [Boaz].","Honor your father and your [mother]."],
["RUTH","NAOMI","BOAZ","HONOR","GRAIN","LOYAL"],[("Did Ruth leave Naomi?",["Yes","No"],1),("Who was Ruth’s great-grandson?",["King David","Moses"],0)],
"Draw Ruth gathering grain for Naomi.",("Ephesians 6:2","“Honor your father and mother.”"),
scene(sun(560,56),wheat(380,620),person(160,beard=False,arms="open",hair="wrap"),person(290,beard=False,arms="mixed",hair="wrap",s=.85),label="Coloring picture: Ruth and Naomi with the grain fields"))
ALL[-1]['cat']=dict(part="The Fourth Commandment",text="Thou shalt honor thy father and thy mother, that it may be well with thee, and thou mayest live long on the earth.",mean="We should fear and love God that we may not despise nor anger our parents and those in authority over us, but give them honor, serve, obey, love, and esteem them.")

D("2027-01-15",S,"The Good Samaritan","a 3rd–5th grader","Luke 10:33–34",[(33,"But a Samaritan, as he journeyed, came to where he was, and when he saw him, he had compassion."),(34,"He went to him and bound up his wounds, pouring on oil and wine. Then he set him on his own animal and brought him to an inn and took care of him.")],
"Who is my neighbor?",[
"The Fifth Commandment is “You shall not murder.” Jesus said it also means we shouldn’t hate or hurt anyone with angry words. And it means more than just not hurting people. God wants us to help our neighbors in every need.",
"A man asked Jesus, “Who is my neighbor?” So Jesus told a story. A man was walking from Jerusalem to Jericho when robbers attacked him, beat him up, and left him half dead by the road. A priest came by, saw him, and walked past on the other side. Then a temple helper came by, looked, and walked past too.",
"Then a Samaritan came by. Jews and Samaritans didn’t get along at all. But the Samaritan felt sorry for him. He bandaged his wounds, put him on his own donkey, took him to an inn, and paid for him to be cared for. Jesus asked, “Which one was a neighbor?” “The one who showed mercy.” Jesus said, “Go and do likewise.”"],
"Help and befriend",["Luther says we should “help and befriend him in every bodily need.” Jesus is the best Good Samaritan. He found us hurt by sin, and He paid everything to heal us. Now He sends us to help anyone who needs us."],
["Who walked past the hurt man? Who stopped to help?","What did the Samaritan do for the man?","The Fifth Commandment is about more than not hurting people. How can we help someone in need this week?"],
"Lord Jesus, thank You for stopping to rescue us when we were hurt by sin. Forgive us for angry words and for walking past people who need help.","Make us good neighbors who help and befriend people in every need.",
"The Good Samaritan stopped to help a hurt man. Jesus said, “Go and do likewise!”",
["Robbers [hurt] the man.","A [priest] walked past.","A [Samaritan] stopped to help.","He put him on his own [donkey].","Jesus said, “Go and do [likewise].”"],
["SAMARITAN","NEIGHBOR","MERCY","DONKEY","INN","HELP"],[("Who helped the hurt man?",["The Samaritan","The priest"],0),("Who is our neighbor?",["Anyone who needs help","Only our friends"],0)],
"Draw the Good Samaritan helping the man.",("Luke 10:37","“You go, and do likewise.”"),
scene(sun(560,56),hills(),donkey(470),person(270,beard=True,arms="open",hair="wrap",s=.85),'<ellipse cx="170" cy="290" rx="60" ry="12"/><circle cx="120" cy="284" r="11"/>',label="Coloring picture: the Good Samaritan helping a hurt man"))
ALL[-1]['cat']=dict(part="The Fifth Commandment",text="Thou shalt not kill.",mean="We should fear and love God that we may not hurt nor harm our neighbor in his body, but help and befriend him in every bodily need.")

D("2027-01-16",S,"The Wedding at Cana","Mom or Dad","John 2:11",[(11,"This, the first of his signs, Jesus did at Cana in Galilee, and manifested his glory. And his disciples believed in him.")],
"Water into wine",[
"The Sixth Commandment is “You shall not commit adultery.” That’s a grown-up word, but here’s what it means: God made marriage as a lifelong gift for a husband and wife. He wants husbands and wives to love and honor each other, and He wants all of us to keep our words and actions pure and decent.",
"Jesus showed how much He honors marriage by going to a wedding party in the town of Cana. In the middle of the celebration, the wine ran out! That would have been very embarrassing for the bride and groom. Mary told Jesus, and then she told the servants, “Do whatever He tells you.”",
"Jesus had the servants fill six huge stone jars with water, all the way to the top. Then He said, “Draw some out and take it to the man in charge.” The water had become wine, and the best wine of the party! It was Jesus’ very first miracle, and He did it to bless a husband and wife on their wedding day."],
"God’s gift of marriage",["Jesus began His miracles at a wedding, because marriage is God’s good gift, from the very beginning in the garden. That’s why we keep our words and actions pure, pray for married couples, and thank God for moms and dads who love each other."],
["Where was the wedding? What ran out?","What did Jesus turn the water into?","Why do you think Jesus did His first miracle at a wedding? What does that say about marriage?"],
"Lord Jesus, thank You for blessing the wedding at Cana, and for the gift of marriage. Bless every husband and wife in our family.","Help us keep our words and actions pure, and help husbands and wives love and honor each other.",
"Jesus turned water into wine at a wedding. It was His first miracle!",
["Jesus went to a [wedding].","The [wine] ran out.","Mary said, “Do whatever He tells [you].”","Jesus turned [water] into wine.","God made [marriage] as a gift."],
["WEDDING","CANA","WATER","WINE","JARS","MARRIAGE"],[("What was Jesus’ first miracle?",["Water into wine","Walking on water"],0),("Is marriage a gift from God?",["Yes","No"],0)],
"Draw the six big water jars at the wedding.",("John 2:11","“This, the first of his signs, Jesus did at Cana in Galilee.”"),
scene(*[f'<path d="M{x-18},300 q-10,-34 4,-52 h28 q14,18 4,52 Z M{x-12},248 v-8 h24 v8"/>' for x in (110,170,230,410,470,530)],person(320,beard=True,arms="open",hair="short",s=.85),label="Coloring picture: the six water jars at the wedding in Cana"))
ALL[-1]['cat']=dict(part="The Sixth Commandment",text="Thou shalt not commit adultery.",mean="We should fear and love God that we may lead a chaste and decent life in words and deeds, and that husband and wife love and honor each other.")

D("2027-01-17",S,"Zacchaeus","a K–2nd grader, with help","Luke 19:8",[(8,"And Zacchaeus stood and said to the Lord, “Behold, Lord, the half of my goods I give to the poor. And if I have defrauded anyone of anything, I restore it fourfold.”")],
"The man in the tree",[
"The Seventh Commandment is “You shall not steal.” That means we don’t take what isn’t ours, and we don’t cheat people. Instead, we help our neighbors take care of their things.",
"Zacchaeus was a tax collector in the city of Jericho. He was rich, because he cheated people and took extra money for himself. Nobody liked him. One day Jesus came to town, and a huge crowd gathered. Zacchaeus wanted to see Jesus, but he was too short to see over the crowd! So he ran ahead and climbed a sycamore tree.",
"When Jesus came by, He stopped, looked up, and said, “Zacchaeus, hurry and come down. I must stay at your house today!” Zacchaeus hurried down, full of joy. The crowd grumbled, but Zacchaeus was changed. He said, “I’ll give half of what I own to the poor. And if I cheated anyone, I’ll pay them back four times as much!” Jesus said, “Today salvation has come to this house.”"],
"Jesus changes hearts",["Jesus didn’t tell Zacchaeus to stop stealing first and then He would come over. Jesus came to him first, with love and forgiveness, and that changed Zacchaeus’s heart. Jesus came “to seek and to save the lost.”"],
["Why did Zacchaeus climb a tree? What did Jesus say to him?","What did Zacchaeus promise to do?","Jesus loved Zacchaeus before he changed. How did that love change him?"],
"Lord Jesus, thank You for seeking and saving the lost, like Zacchaeus, and like us. Forgive us for the times we take what isn’t ours.","Help us be honest, and help us take care of other people’s things.",
"Zacchaeus climbed a tree to see Jesus. Jesus came to his house, and Zacchaeus paid back everyone he cheated!",
["Zacchaeus was a tax [collector].","He was too [short] to see.","He climbed a sycamore [tree].","Jesus said, “I must stay at your [house].”","He paid people back four [times] as much."],
["ZACCHAEUS","TREE","SHORT","JERICHO","HONEST","LOST"],[("Why did Zacchaeus climb the tree?",["To see Jesus","To pick fruit"],0),("Did Jesus love Zacchaeus?",["Yes","No"],0)],
"Draw Zacchaeus up in the sycamore tree.",("Luke 19:10","“The Son of Man came to seek and to save the lost.”"),
scene(sun(560,56),tree(250,220),'<g transform="translate(0,-120)">'+person(250,beard=True,arms="up",hair="short",s=.4)+'</g>',person(430,beard=True,arms="up",hair="short",s=.9),label="Coloring picture: Zacchaeus in the sycamore tree"))
ALL[-1]['cat']=dict(part="The Seventh Commandment",text="Thou shalt not steal.",mean="We should fear and love God that we may not take our neighbor’s money or goods, nor get them by false ware or dealing, but help him to improve and protect his property and business.")

D("2027-01-18",S,"A True Friend","an older kid","1 Samuel 19:4",[(4,"And Jonathan spoke well of David to Saul his father and said to him, “Let not the king sin against his servant David, because he has not sinned against you, and because his deeds have brought good to you.")],
"Jonathan speaks up",[
"The Eighth Commandment is “You shall not give false testimony against your neighbor.” That means no lying about people, no gossip, and no saying mean things behind their backs. Instead, we defend them, speak well of them, and explain everything in the kindest way.",
"After David defeated Goliath, King Saul’s son Jonathan became David’s best friend. But King Saul grew jealous of David, because the people loved him. Saul even told his servants to kill David!",
"Jonathan could have stayed quiet. Saul was his dad, and the king! But Jonathan went to his father and spoke up: “Don’t do wrong to David. He hasn’t done anything wrong to you. He risked his life to fight Goliath, and you were glad!” Saul listened that time and promised not to hurt David. Jonathan protected his friend’s good name, even when it was hard."],
"Speak well of others",["It’s easy to join in when people talk badly about someone. Jonathan shows us a better way: stand up for people and say what’s good about them. And Jesus does that for us. He speaks up for us before the Father, even though we’ve sinned."],
["Who was David’s best friend? Why was Saul angry with David?","What did Jonathan say to his father?","Why is it hard to defend someone when others are talking badly about them? What could you say?"],
"Lord Jesus, thank You for speaking up for us before the Father. Thank You for true friends like Jonathan. Forgive us for gossip and unkind words.","Help us defend others, speak well of them, and explain everything in the kindest way.",
"Jonathan stood up for his friend David. He spoke well of him to King Saul!",
["Jonathan was David’s best [friend].","King [Saul] was jealous of David.","Jonathan [spoke] well of David.","We should not tell [lies] about others.","We should [defend] our neighbor."],
["JONATHAN","DAVID","SAUL","FRIEND","TRUTH","DEFEND"],[("Did Jonathan stay quiet?",["Yes","No"],1),("What should we do when others gossip?",["Speak well of people","Join in"],0)],
"Draw Jonathan and David, best friends.",("Exodus 20:16","“You shall not bear false witness against your neighbor.”"),
scene(throne(500),person(500,beard=True,arms="mixed",hair="short",s=.85),crown(500,126),person(200,beard=False,arms="open",hair="curly"),person(330,beard=False,arms="open",hair="short",s=.9),label="Coloring picture: Jonathan speaking up for David before King Saul"))
ALL[-1]['cat']=dict(part="The Eighth Commandment",text="Thou shalt not bear false witness against thy neighbor.",mean="We should fear and love God that we may not deceitfully belie, betray, slander, or defame our neighbor, but defend him, speak well of him, and put the best construction on everything.")

D("2027-01-19",S,"Naboth’s Vineyard","a 3rd–5th grader","Hebrews 13:5",[(5,"Keep your life free from love of money, and be content with what you have, for he has said, “I will never leave you nor forsake you.”")],
"The king who pouted",[
"The Ninth and Tenth Commandments are about coveting. To covet means to want something that belongs to someone else so badly that it fills your heart. The Ninth Commandment says, “You shall not covet your neighbor’s house.”",
"King Ahab had a palace, money, and everything a king could want. But next door was a vineyard owned by a man named Naboth. Ahab said, “Give me your vineyard. I’ll pay you for it.” Naboth said, “No, this land has been in my family for generations. God gave it to us.” So Ahab went home, lay on his bed, turned his face to the wall, and refused to eat. A grown king, pouting!",
"Then his wicked wife Jezebel came up with a plan. She paid men to tell lies about Naboth, and Naboth was put to death. Ahab took the vineyard. But God saw everything. He sent Elijah to tell Ahab that God would judge him for this great evil. Coveting started in Ahab’s heart, and it led to lying, stealing, and much worse."],
"Be content",["Coveting starts small, inside, where nobody sees. That’s why God gave a commandment about our hearts. The cure is contentment: trusting that God gives us what we need. He promises, “I will never leave you nor forsake you.” With Jesus, we already have the best thing."],
["What did Ahab want? What did Naboth say?","What did Ahab do when he couldn’t have it?","Why does God care about what we want in our hearts, not just what we do? What helps us be content?"],
"Heavenly Father, thank You for giving us everything we need, and for promising never to leave us. Forgive us for wanting what belongs to others.","Give us content hearts that trust You.",
"King Ahab coveted Naboth’s vineyard and pouted. God wants us to be content with what we have!",
["King [Ahab] wanted Naboth’s vineyard.","Naboth said, “[No].”","Ahab lay on his bed and [pouted].","To covet means to want what is someone [else]’s.","Be [content] with what you have."],
["AHAB","NABOTH","VINEYARD","COVET","CONTENT","ELIJAH"],[("Was Ahab content?",["Yes","No"],1),("Will God ever leave us?",["Yes","No"],1)],
"Draw something you’re thankful to have, instead of wanting more.",("Hebrews 13:5","“Be content with what you have.”"),
scene(sun(560,56),vines(300,620),house(140),person(250,beard=True,arms="mixed",hair="short",s=.7),label="Coloring picture: Naboth’s vineyard next to the palace"))
ALL[-1]['cat']=dict(part="The Ninth Commandment",text="Thou shalt not covet thy neighbor’s house.",mean="We should fear and love God that we may not craftily seek to get our neighbor’s inheritance or house, nor obtain it by a show of right, but help and be of service to him in keeping it.")

D("2027-01-20",S,"Lot Chooses","an older kid","Philippians 4:11",[(11,"Not that I am speaking of being in need, for I have learned in whatever situation I am to be content.")],
"Abram lets Lot pick",[
"The Tenth Commandment is “You shall not covet your neighbor’s wife, or his workers, or his animals, or anything that is your neighbor’s.” It’s the last commandment, and it reaches all the way into our hearts.",
"Abram and his nephew Lot both had so many sheep, goats, and cattle that their shepherds started fighting over the land. Abram said, “Let’s not fight. We’re family. You choose first. If you go left, I’ll go right.” That was generous! Abram was older, and God had promised the land to him.",
"Lot looked out and saw the Jordan Valley, green and well-watered like a garden. He wanted it! So he chose the best land for himself and moved his tents near the city of Sodom, a very wicked place. Lot’s choice brought him a lot of trouble later. But God blessed Abram and told him, “Look in every direction. All this land I will give to you.”"],
"Learning contentment",["Paul wrote that he had learned to be content whether he had a lot or a little. Contentment is learned, and God teaches it to us. That’s the end of the Ten Commandments. They show us how to love God and our neighbor, and they show us our sin. And they point us to Jesus, who kept every one of them for us."],
["What did Abram let Lot do? What did Lot choose?","Was Abram generous? How?","We’ve learned all Ten Commandments. Which is hardest for you? Who kept them all perfectly for us?"],
"Lord God, thank You for Your good commandments, and for Jesus, who kept them all for us. Forgive us for every commandment we’ve broken.","Teach us to be content and generous, like Abram.",
"Abram let Lot choose first. Lot wanted the best land, but God blessed Abram!",
["Abram and [Lot] had too many animals.","Abram let Lot choose [first].","Lot chose the green [valley].","Paul learned to be [content].","[Jesus] kept all the commandments for us."],
["ABRAM","LOT","CHOOSE","VALLEY","CONTENT","GENEROUS"],[("Who chose first?",["Lot","Abram"],0),("Who kept all ten commandments for us?",["Jesus","Abram"],0)],
"Draw the Ten Commandments on two stone tablets.",("Philippians 4:11","“I have learned in whatever situation I am to be content.”"),
scene(sun(560,56),mountains(),tent(150),person(300,beard=True,arms="open",hair="wrap",s=.85),person(420,beard=True,arms="mixed",hair="short",s=.85),sheep(540,.7),label="Coloring picture: Abram and Lot looking at the land"))
ALL[-1]['cat']=dict(part="The Tenth Commandment",text="Thou shalt not covet thy neighbor’s wife, nor his manservant, nor his maidservant, nor his cattle, nor anything that is thy neighbor’s.",mean="We should fear and love God that we may not estrange, force, or entice away from our neighbor his wife, workers, or animals, but urge them to stay and do their duty.")

S="Small Catechism: The Creed"
D("2027-01-21",S,"Look at the Birds","a K–2nd grader, with help","Matthew 6:26",[(26,"Look at the birds of the air: they neither sow nor reap nor gather into barns, and yet your heavenly Father feeds them. Are you not of more value than they?")],
"God our Father, Maker of everything",[
"After the Ten Commandments, the Small Catechism teaches the Apostles’ Creed. The Creed is what Christians all over the world have believed for almost two thousand years. It has three parts, called articles. The First Article is about God the Father, who made us.",
"One day Jesus sat on a hillside and taught a big crowd. He said, “Don’t worry about what you will eat or drink or wear. Look at the birds! They don’t plant seeds or harvest crops, but your heavenly Father feeds them. Aren’t you worth more than birds?”",
"“And look at the flowers in the field. They don’t work or sew clothes. But even King Solomon in all his fancy robes wasn’t dressed as beautifully as one of them. If God takes such good care of flowers, won’t He take care of you?” Luther says God gives us “clothing and shoes, food and drink, house and home,” every day."],
"He richly provides",["Luther’s explanation of the First Article lists everything God gives us: our bodies, eyes and ears, food, clothes, home, family, and protection. All of it comes “purely out of fatherly, divine goodness and mercy.” We didn’t earn it. That’s why we thank and praise Him."],
["What did Jesus tell us to look at? Who feeds the birds?","What are some things God gives you every day?","Why do you think Jesus tells us not to worry? What do you tend to worry about?"],
"Heavenly Father, thank You for making us and for giving us everything we need every day, purely out of Your goodness. You take care of the birds, and You take care of us.","When we start to worry, remind us that You are our Father.",
"Jesus said, “Look at the birds! Your heavenly Father feeds them.” God takes care of us, too!",
["The Creed has three [articles].","The First Article is about God the [Father].","God feeds the [birds].","God dresses the [flowers] beautifully.","We don’t need to [worry]."],
["CREED","FATHER","BIRDS","FLOWERS","MAKER","WORRY"],[("Who feeds the birds?",["God","Nobody"],0),("Are you worth more than birds to God?",["Yes","No"],0)],
"Draw birds in the sky and flowers in the field.",("Matthew 6:26","“Your heavenly Father feeds them.”"),
scene(sun(560,60),cloud(120,70),bird(260,70),bird(320,50),bird(380,80),bird(450,60),flower(100),flower(160,80),flower(220,50),flower(430,70),flower(500,90),flower(570,60),person(320,beard=True,arms="open",hair="short",s=.8),label="Coloring picture: birds and flowers that God cares for"))
ALL[-1]['cat']=dict(part="The First Article",text="I believe in God the Father Almighty, Maker of heaven and earth.",mean="I believe that God has made me and all creatures; that He has given me my body and soul, eyes, ears, and all my members, my reason and all my senses, and still preserves them; also clothing and shoes, food and drink, house and home, and all my goods; that He richly and daily provides me with all that I need to support this body and life; that He defends me against all danger, and guards and protects me from all evil; and all this purely out of fatherly, divine goodness and mercy, without any merit or worthiness in me; for all which it is my duty to thank and praise, to serve and obey Him. This is most certainly true.")

D("2027-01-22",S,"Not with Silver or Gold","an older kid","1 Peter 1:18–19",[(18,"knowing that you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold,"),(19,"but with the precious blood of Christ, like that of a lamb without blemish or spot.")],
"Barabbas goes free",[
"The Second Article of the Creed is about Jesus, God’s Son, who was born, died, and rose again to save us. Luther says Jesus “redeemed me,” which means He bought me back, “not with gold or silver, but with His holy, precious blood.”",
"On the morning Jesus was crucified, Pilate, the Roman governor, had a custom: at Passover he would set one prisoner free. In prison sat a man named Barabbas, a robber who had murdered someone. Pilate asked the crowd, “Whom do you want me to release: Barabbas, or Jesus?” The crowd shouted, “Barabbas!”",
"So Barabbas, who deserved to die, walked out free. And Jesus, who had done nothing wrong, carried His cross to the hill and died in Barabbas’s place. But Barabbas wasn’t the only one Jesus died for. Jesus took our place too. And on the third day, He rose from the dead!"],
"That I may be His own",["Luther says Jesus did all this “that I may be His own, and live under Him in His kingdom.” You were bought at a price, the highest price ever paid. That’s how much you are worth to Jesus. You belong to Him."],
["Who did the crowd want set free? Who died in his place?","What did Jesus use to buy us back?","How are we like Barabbas? What does it mean that we belong to Jesus?"],
"Lord Jesus, thank You for redeeming us, not with gold or silver, but with Your holy, precious blood. Thank You for taking our place.","Help us live as Your own, in Your kingdom, every day.",
"Barabbas went free, and Jesus died in his place. Jesus bought us back with His precious blood!",
["The Second Article is about [Jesus].","The crowd chose [Barabbas].","Jesus died in his [place].","He bought us with His precious [blood].","On the third day, Jesus [rose]!"],
["JESUS","REDEEMED","CROSS","BLOOD","BARABBAS","ROSE"],[("Who deserved to die?",["Barabbas","Jesus"],0),("What did Jesus pay to save us?",["His blood","Gold"],0)],
"Draw the three crosses on the hill, and the sun rising on Easter.",("1 Peter 1:19","“With the precious blood of Christ, like that of a lamb.”"),
scene(sun(560,60),hills(),crosses(),label="Coloring picture: three crosses on a hill"))
ALL[-1]['cat']=dict(part="The Second Article",text="And in Jesus Christ, His only Son, our Lord; who was conceived by the Holy Ghost, born of the Virgin Mary; suffered under Pontius Pilate, was crucified, dead, and buried; He descended into hell; the third day He rose again from the dead; He ascended into heaven, and sitteth on the right hand of God the Father Almighty; from thence He shall come to judge the quick and the dead.",mean="I believe that Jesus Christ, true God, begotten of the Father from eternity, and also true man, born of the Virgin Mary, is my Lord, who has redeemed me, a lost and condemned creature, purchased and won me from all sins, from death, and from the power of the devil; not with gold or silver, but with His holy, precious blood and with His innocent suffering and death; that I may be His own, and live under Him in His kingdom, and serve Him in everlasting righteousness, innocence, and blessedness, even as He is risen from the dead, lives and reigns to all eternity. This is most certainly true.")

D("2027-01-23",S,"Tongues of Fire","a 3rd–5th grader","Acts 2:38–39",[(38,"And Peter said to them, “Repent and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins, and you will receive the gift of the Holy Spirit."),(39,"For the promise is for you and for your children and for all who are far off, everyone whom the Lord our God calls to himself.”")],
"Pentecost",[
"The Third Article of the Creed is about the Holy Spirit. Luther says, “I cannot by my own reason or strength believe in Jesus Christ, my Lord, or come to Him.” We can’t make ourselves believe. The Holy Spirit gives us faith through God’s Word.",
"Fifty days after Easter, the disciples were together in Jerusalem. Suddenly there was a sound like a mighty rushing wind, and what looked like flames of fire rested on each one of them. They were filled with the Holy Spirit and began speaking in other languages! Visitors from all over the world heard them telling about God’s mighty works in their own languages.",
"Then Peter stood up and preached about Jesus, crucified and risen. The people’s hearts were cut, and they asked, “What should we do?” Peter said, “Repent and be baptized, and you will receive the gift of the Holy Spirit. For the promise is for you and for your children.” That day about three thousand people were baptized!"],
"For you and your children",["The Holy Spirit called those people by the gospel, and He calls us the same way, through God’s Word and Baptism. Peter said the promise is “for you and for your children.” That’s why we baptize babies, and why we gather for devotions: the Spirit works through the Word."],
["What did the disciples hear and see at Pentecost? How many were baptized?","Can we make ourselves believe? Who gives us faith?","Peter said the promise is “for your children.” What does that mean for the kids in our family?"],
"Holy Spirit, thank You for calling us by the gospel and giving us faith. Thank You that Your promise is for us and our children.","Keep us in the true faith, and work through Your Word in our home.",
"At Pentecost the Holy Spirit came with wind and fire! Peter said the promise is for you and your children.",
["The Third Article is about the Holy [Spirit].","They heard a sound like [wind].","Flames of [fire] rested on them.","Peter said, “Repent and be [baptized].”","The promise is for you and your [children]."],
["PENTECOST","SPIRIT","WIND","FIRE","PETER","PROMISE"],[("Can we make ourselves believe by our own strength?",["Yes","No"],1),("Is God’s promise for children?",["Yes","No"],0)],
"Draw the disciples with flames of fire above their heads.",("Acts 2:39","“The promise is for you and for your children.”"),
scene(person(160,beard=True,arms="up",hair="short",s=.8),person(270,beard=True,arms="open",hair="curly",s=.8),person(380,beard=False,arms="up",hair="wrap",s=.8),person(490,beard=True,arms="open",hair="short",s=.8),flames(160,136,30),flames(270,136,30),flames(380,136,30),flames(490,136,30),'<path d="M40,60 q60,-20 120,0 q60,20 120,0 M360,50 q60,-20 120,0 q60,20 120,0" fill="none"/>',label="Coloring picture: the disciples at Pentecost with tongues of fire"))
ALL[-1]['cat']=dict(part="The Third Article",text="I believe in the Holy Ghost; the holy Christian Church, the communion of saints; the forgiveness of sins; the resurrection of the body; and the life everlasting. Amen.",mean="I believe that I cannot by my own reason or strength believe in Jesus Christ, my Lord, or come to Him; but the Holy Ghost has called me by the Gospel, enlightened me with His gifts, sanctified and kept me in the true faith; even as He calls, gathers, enlightens, and sanctifies the whole Christian Church on earth, and keeps it with Jesus Christ in the one true faith. In this Christian Church He daily and richly forgives all sins to me and all believers, and at the last day will raise up me and all the dead, and will give unto me and all believers in Christ eternal life. This is most certainly true.")

S="Small Catechism: The Lord’s Prayer"
D("2027-01-24",S,"Lord, Teach Us to Pray","Mom or Dad","Luke 11:1",[(1,"Now Jesus was praying in a certain place, and when he finished, one of his disciples said to him, “Lord, teach us to pray, as John taught his disciples.”")],
"Our Father",[
"Now we come to the Lord’s Prayer, the prayer Jesus Himself taught us. The disciples often saw Jesus go off by Himself to pray. One day, when He finished, they asked Him, “Lord, teach us to pray.”",
"Jesus said, “When you pray, say: Our Father in heaven.” That was surprising! People knew God as the mighty King and Creator. But Jesus told them to call God “Father,” even “Abba,” which is like saying “Dad.” Then Jesus taught them the rest of the prayer, seven requests in all.",
"Jesus also told a story. “Which father, if his son asks for a fish, would give him a snake instead? If you, who are sinners, know how to give good gifts to your children, how much more will your Father in heaven give good things to those who ask Him!”"],
"Dear children, dear Father",["Luther says that with the words “Our Father,” God “tenderly invites us” to talk to Him “as dear children ask their dear father.” Think about how you ask Mom or Dad for something. You don’t need fancy words. You can talk to God that way too."],
["What did the disciples ask Jesus? What did Jesus tell them to call God?","How many requests are in the Lord’s Prayer?","Why do you think Jesus wants us to call God “Father”? How does that change the way you pray?"],
"Our Father in heaven, thank You for inviting us to talk to You like dear children talk to their dad. Thank You for teaching us to pray.","Teach us to pray with boldness and confidence every day.",
"Jesus taught His disciples to pray, “Our Father.” We can talk to God like children talk to their dad!",
["The disciples said, “Lord, [teach] us to pray.”","Jesus told us to call God our [Father].","“Abba” is like saying “[Dad].”","The Lord’s Prayer has [seven] requests.","God gives [good] gifts to His children."],
["PRAYER","FATHER","ABBA","HEAVEN","CHILDREN","TEACH"],[("What did Jesus tell us to call God?",["Father","Sir"],0),("Do we need fancy words to pray?",["Yes","No"],1)],
"Draw your family praying together.",("Luke 11:2","“When you pray, say: ‘Father, hallowed be your name.’”"),
scene(sun(560,56),hills(),rock(320),person(320,beard=True,arms="open",hair="short",s=.8),person(150,beard=True,arms="mixed",hair="curly",s=.75),person(470,beard=False,arms="open",hair="wrap",s=.75),label="Coloring picture: Jesus teaching the disciples to pray"))
ALL[-1]['cat']=dict(part="The Introduction",text="Our Father who art in heaven.",mean="God would by these words tenderly invite us to believe that He is our true Father, and that we are His true children, so that we may with all boldness and confidence ask Him as dear children ask their dear father.")

D("2027-01-25",S,"Daniel Prays","a 3rd–5th grader","Daniel 6:10",[(10,"When Daniel knew that the document had been signed, he went to his house where he had windows in his upper chamber open toward Jerusalem. He got down on his knees three times a day and prayed and gave thanks before his God, as he had done previously.")],
"The lions’ den",[
"The First Petition of the Lord’s Prayer is “Hallowed be Thy name.” Hallowed means holy. God’s name is already holy, but we pray that it would be kept holy among us, by our teaching God’s Word truly and living as His children.",
"Daniel served King Darius in Babylon, and he did such a great job that the other officials got jealous. They tricked the king into making a law: for thirty days, anyone who prayed to any god except the king would be thrown into a den of lions. Daniel knew about the law. But he went home, opened his window toward Jerusalem, knelt down, and prayed to God three times a day, just like always.",
"The officials caught him, and the sad king had to throw Daniel into the lions’ den. But God sent His angel to shut the lions’ mouths! In the morning Daniel called out, “My God sent His angel, and I am safe!” Then King Darius made a new law: everyone in his kingdom must honor the God of Daniel, “for He is the living God.” God’s name was hallowed in the whole kingdom."],
"Hallowed among us",["Daniel kept praying to the true God, and because of his faithful life, a whole kingdom heard God’s name. Luther says God’s name is hallowed “when the Word of God is taught in its truth and purity, and we, as the children of God, also lead holy lives in accordance with it.”"],
["What law did the king make? What did Daniel do anyway?","How did God protect Daniel?","Because of Daniel, the king honored God’s name. How can our family help people honor God’s name?"],
"Holy God, hallowed be Your name! Thank You for protecting Daniel, and for keeping Your name holy among us through Your Word.","Help us live as Your children, so that others will honor Your name.",
"Daniel kept praying, and God shut the lions’ mouths! Then the king honored the name of Daniel’s God.",
["Daniel prayed [three] times a day.","He opened his [window] toward Jerusalem.","He was thrown into a den of [lions].","God sent His [angel] to shut their mouths.","Hallowed means [holy]."],
["DANIEL","LIONS","WINDOW","HALLOWED","PRAY","ANGEL"],[("Did Daniel stop praying?",["Yes","No"],1),("Who shut the lions’ mouths?",["God’s angel","The king"],0)],
"Draw Daniel praying at his open window.",("Daniel 6:10","“He got down on his knees three times a day and prayed.”"),
scene(window(400),stars(6,41,(380,540)),person(250,beard=True,arms="open",hair="short",s=.7),'<path d="M150,300 h200" fill="none"/>',label="Coloring picture: Daniel praying at his open window"))
ALL[-1]['cat']=dict(part="The First Petition",text="Hallowed be Thy name.",mean="God’s name is indeed holy in itself; but we pray in this petition that it may become holy among us also.")

D("2027-01-26",S,"The Mustard Seed","a K–2nd grader, with help","Matthew 13:31–32",[(31,"He put another parable before them, saying, “The kingdom of heaven is like a grain of mustard seed that a man took and sowed in his field."),(32,"It is the smallest of all seeds, but when it has grown it is larger than all the garden plants and becomes a tree, so that the birds of the air come and make nests in its branches.”")],
"A tiny seed",[
"The Second Petition is “Thy kingdom come.” God’s kingdom isn’t a country on a map. It’s wherever Jesus rules as King, in people’s hearts, through His Word. We pray that His kingdom would come to us and to many more people.",
"Jesus told a story about God’s kingdom. A man planted a mustard seed in his field. A mustard seed is tiny, about as small as the period at the end of this sentence! But it grew, and grew, and grew, until it became a big plant like a tree, so big that birds came and built nests in its branches.",
"That’s how God’s kingdom works. It started small: a baby in a manger, twelve disciples, a few believers in Jerusalem. But the Holy Spirit kept spreading God’s Word, and the kingdom grew and grew until it filled the whole world. And it’s still growing today."],
"Thy kingdom come",["Luther says God’s kingdom comes “when our heavenly Father gives us His Holy Spirit, so that by His grace we believe His holy Word and lead godly lives.” A little bit of faith, like a tiny seed, can grow. And God’s kingdom will fully come when Jesus comes again."],
["How big is a mustard seed? What did it grow into?","How did God’s kingdom start small and grow big?","Where does Jesus rule as King? How do we pray for His kingdom to come?"],
"Lord Jesus, our King, thank You for growing Your kingdom from tiny beginnings all over the world. Thy kingdom come!","Grow our faith like a mustard seed, and bring Your kingdom to many more people.",
"Jesus said God’s kingdom is like a tiny mustard seed that grows into a big tree!",
["A mustard seed is very [tiny].","It grew into a big [tree].","[Birds] built nests in its branches.","We pray, “Thy [kingdom] come.”","Jesus is our [King]."],
["MUSTARD","SEED","TREE","KINGDOM","GROW","BIRDS"],[("Did the tiny seed stay tiny?",["Yes","No"],1),("Who is the King of God’s kingdom?",["Jesus","A farmer"],0)],
"Draw a tiny seed, then the big tree it grew into, with birds.",("Matthew 13:31","“The kingdom of heaven is like a grain of mustard seed.”"),
scene(sun(560,56),tree(380,240),bird(330,110),bird(420,90),bird(460,130),seed(120,290),'<path d="M120,286 q-20,-30 -40,-34 M120,286 q24,-40 52,-50" fill="none" stroke-dasharray="4 5"/>',person(160,beard=True,arms="mixed",hair="wrap",s=.7),label="Coloring picture: a tiny mustard seed and the big tree it becomes"))
ALL[-1]['cat']=dict(part="The Second Petition",text="Thy kingdom come.",mean="The kingdom of God comes indeed without our prayer, of itself; but we pray in this petition that it may come unto us also.")

D("2027-01-27",S,"Not My Will","an older kid","Luke 22:42",[(42,"saying, “Father, if you are willing, remove this cup from me. Nevertheless, not my will, but yours, be done.”")],
"In the garden",[
"The Third Petition is “Thy will be done on earth as it is in heaven.” God’s will is always good and gracious. We pray that His will would be done among us, and that He would stop everything that fights against it, like the devil, the world, and our own sinful wants.",
"On the night before He died, after the Last Supper, Jesus went to a garden called Gethsemane with His disciples. He knew what was coming: the cross. He went a little way off, knelt down, and prayed so hard that His sweat was like drops of blood.",
"Jesus prayed, “Father, if You are willing, take this cup away from Me. Nevertheless, not My will, but Yours, be done.” An angel came to strengthen Him. Then Jesus stood up and went to the cross, because it was the Father’s will to save us, and Jesus loved us too much to say no."],
"Thy will be done",["Jesus prayed the Third Petition in the hardest moment of His life, and He meant it. When we pray “Thy will be done,” we’re trusting that God’s plan is better than ours, even when we don’t understand it. And His will for you is good: He wants you saved and with Him forever."],
["Where did Jesus pray? What did He ask the Father?","What did Jesus say after “take this cup away”?","Why is it hard to pray “Your will be done” sometimes? Why can we trust God’s will?"],
"Heavenly Father, Thy will be done. Thank You, Lord Jesus, for obeying the Father’s will and going to the cross for us.","When things are hard, help us trust that Your will is good and gracious.",
"In the garden, Jesus prayed, “Not My will, but Yours, be done.” Then He went to the cross for us.",
["Jesus prayed in a [garden].","The garden was called [Gethsemane].","Jesus said, “Not My [will], but Yours.”","An [angel] came to strengthen Him.","God’s will is good and [gracious]."],
["GARDEN","WILL","PRAYER","ANGEL","CUP","OBEY"],[("Did Jesus obey the Father?",["Yes","No"],0),("Is God’s will good?",["Yes","No"],0)],
"Draw Jesus praying by a big rock in the garden at night.",("Luke 22:42","“Not my will, but yours, be done.”"),
scene(moon(560,56),stars(10,63,(500,620)),tree(110,180),tree(540,150),rock(330),person(330,beard=True,arms="up",hair="short",s=.7),label="Coloring picture: Jesus praying in the garden of Gethsemane"))
ALL[-1]['cat']=dict(part="The Third Petition",text="Thy will be done on earth as it is in heaven.",mean="The good and gracious will of God is done indeed without our prayer; but we pray in this petition that it may be done among us also.")

D("2027-01-28",S,"A Boy’s Lunch","a 3rd–5th grader","John 6:9, 11",[(9,"“There is a boy here who has five barley loaves and two fish, but what are they for so many?”"),(11,"Jesus then took the loaves, and when he had given thanks, he distributed them to those who were seated. So also the fish, as much as they wanted.")],
"Five loaves and two fish",[
"The Fourth Petition is “Give us this day our daily bread.” Daily bread means everything we need for this life: food, clothes, home, family, health, good weather, good friends, and more. God gives it even to people who never pray. But we pray so that we will know it all comes from Him, and receive it with thanks.",
"A huge crowd followed Jesus out to a hillside, more than five thousand people. It was getting late, and everyone was hungry. Jesus asked Philip, “Where can we buy bread for all these people?” Philip said, “Even a whole bunch of money wouldn’t buy enough!” Then Andrew said, “There’s a boy here with five barley loaves and two fish. But what are they for so many?”",
"Jesus had everyone sit down on the grass. He took the boy’s lunch, gave thanks to God, and passed out the food. And it kept going! Everyone ate as much as they wanted. Afterward the disciples gathered twelve baskets of leftovers. A boy gave Jesus his little lunch, and Jesus fed thousands."],
"With thanksgiving",["Before Jesus passed out the food, He gave thanks. That’s why we pray before meals. Every meal is daily bread from our Father. And the boy shows us that when we give Jesus what we have, even if it’s small, He can do great things with it."],
["What did the boy have? How many people ate?","How many baskets were left over?","What did Jesus do before passing out the food? What are some kinds of daily bread God gives us besides food?"],
"Heavenly Father, give us this day our daily bread. Thank You for every meal, for our home and family, and for everything we need.","Help us receive our daily bread with thanksgiving, and give what we have to You.",
"A boy gave Jesus five loaves and two fish, and Jesus fed more than five thousand people!",
["A boy had five [loaves] of bread.","He also had two [fish].","Jesus gave [thanks] to God.","They gathered [twelve] baskets of leftovers.","Give us this day our daily [bread]."],
["LOAVES","FISH","BOY","BASKETS","THANKS","BREAD"],[("How many fish did the boy have?",["Two","Ten"],0),("Did everyone get enough to eat?",["Yes","No"],0)],
"Draw the boy giving his lunch to Jesus.",("John 6:9","“There is a boy here who has five barley loaves and two fish.”"),
scene(sun(560,56),hills(),person(380,beard=True,arms="open",hair="short",s=.85),person(250,beard=False,arms="open",hair="curly",s=.55),loaves(60),basket(540),label="Coloring picture: a boy giving his loaves and fish to Jesus"))
ALL[-1]['cat']=dict(part="The Fourth Petition",text="Give us this day our daily bread.",mean="God gives daily bread, indeed without our prayer, even to all the wicked; but we pray in this petition that He would lead us to know it, and to receive our daily bread with thanksgiving.")

D("2027-01-29",S,"Seventy-Seven Times","Mom or Dad","Matthew 18:21–22",[(21,"Then Peter came up and said to him, “Lord, how often will my brother sin against me, and I forgive him? As many as seven times?”"),(22,"Jesus said to him, “I do not say to you seven times, but seventy-seven times.")],
"The servant who wouldn’t forgive",[
"The Fifth Petition is “Forgive us our trespasses, as we forgive those who trespass against us.” We need God’s forgiveness every single day. And because He forgives us so much, we forgive others too.",
"Peter asked Jesus, “How many times should I forgive my brother? Seven times?” Jesus said, “Not seven, but seventy-seven times!” Then He told a story. A servant owed his king ten thousand bags of gold, more than he could ever pay back in a hundred lifetimes. He begged for mercy, and the king forgave the whole debt!",
"But then that servant found a friend who owed him a few dollars. He grabbed him and said, “Pay me what you owe!” His friend begged for mercy, but the servant threw him in jail. When the king heard, he was angry. “I forgave you all that debt. Shouldn’t you have had mercy on your friend, as I had mercy on you?”"],
"Forgiven people forgive",["Our sins against God are like that huge debt, and Jesus paid it all on the cross. The things others do to us are like the few dollars. When it’s hard to forgive a brother or sister, remember how much God has forgiven you. That’s where the power to forgive comes from."],
["How many times did Jesus say to forgive? How much did the first servant owe?","What did the forgiven servant do to his friend?","Why is it hard to forgive? How does remembering God’s forgiveness help us?"],
"Heavenly Father, forgive us our trespasses. Thank You for forgiving our huge debt through Jesus.","Help us forgive each other, as You have forgiven us.",
"Jesus said to forgive seventy-seven times! God forgave our huge debt, so we forgive others.",
["Peter asked, “Should I forgive [seven] times?”","Jesus said, “Seventy-[seven] times.”","The king forgave a huge [debt].","The servant didn’t show [mercy] to his friend.","We forgive because God [forgave] us."],
["FORGIVE","SEVENTY","SEVEN","DEBT","MERCY","KING"],[("Did the king forgive the servant?",["Yes","No"],0),("Should we keep forgiving others?",["Yes","No"],0)],
"Draw two brothers or sisters forgiving each other with a hug.",("Matthew 6:12","“Forgive us our debts, as we also have forgiven our debtors.”"),
scene(throne(470),person(470,beard=True,arms="open",hair="short",s=.85),crown(470,134),person(220,beard=True,arms="up",hair="curly",s=.8),label="Coloring picture: the king forgiving his servant"))
ALL[-1]['cat']=dict(part="The Fifth Petition",text="And forgive us our trespasses, as we forgive those who trespass against us.",mean="We pray in this petition that our Father in heaven would not look upon our sins, nor on their account deny our prayer; for we are worthy of none of the things for which we pray, neither have we deserved them; but that He would grant them all to us by grace; for we daily sin much, and indeed deserve nothing but punishment. So will we also heartily forgive, and readily do good to, those who sin against us.")

D("2027-01-30",S,"It Is Written","an older kid","Matthew 4:4",[(4,"But he answered, “It is written, “‘Man shall not live by bread alone, but by every word that comes from the mouth of God.’”")],
"Jesus is tempted",[
"The Sixth Petition is “Lead us not into temptation.” God never tempts anyone to sin. But the devil, the world, and our own sinful hearts try to pull us away from God. We pray that God would guard us and keep us, so we can stand firm and win the victory.",
"Right after His Baptism, the Spirit led Jesus into the wilderness. For forty days He ate nothing, and He was very hungry. Then the devil came: “If You are the Son of God, tell these stones to become bread.” Jesus answered, “It is written: Man shall not live by bread alone, but by every word that comes from the mouth of God.”",
"The devil tried again, twice. He took Jesus to the top of the temple and said, “Jump! God will catch You.” Then he showed Jesus all the kingdoms of the world: “Bow down to me, and I’ll give You all of it.” Each time Jesus answered with God’s Word: “It is written.” Finally Jesus said, “Be gone, Satan!” and the devil left Him."],
"Our weapon",["Jesus won every battle with the same weapon: God’s Word. That’s our weapon too. When you’re tempted to lie, or be mean, or disobey, you can pray, “Lead us not into temptation,” and remember what God says. And where we fall, Jesus already won the victory for us."],
["How long was Jesus in the wilderness? What did the devil tell Him to do with the stones?","What did Jesus say every time He was tempted?","What temptations do kids face? How can God’s Word help us when we’re tempted?"],
"Lord Jesus, thank You for standing strong against the devil for us. Lead us not into temptation, but guard and keep us.","Fill us with Your Word so we can stand firm when we are tempted.",
"The devil tempted Jesus three times, and each time Jesus answered, “It is written!”",
["Jesus was in the [wilderness] for forty days.","The devil said, “Turn these [stones] into bread.”","Jesus answered, “It is [written].”","Jesus used God’s [Word] to fight.","Lead us not into [temptation]."],
["TEMPTED","DEVIL","WRITTEN","STONES","WORD","VICTORY"],[("What did Jesus use to fight the devil?",["God’s Word","A sword"],0),("Did Jesus give in to temptation?",["Yes","No"],1)],
"Draw Jesus in the wilderness standing strong.",("Matthew 4:4","“Man shall not live by bread alone.”"),
scene(sun(560,60),mountains(),stones(90,3),stones(470,3),person(320,beard=True,arms="mixed",hair="short",s=.9),label="Coloring picture: Jesus in the wilderness"))
ALL[-1]['cat']=dict(part="The Sixth Petition",text="And lead us not into temptation.",mean="God indeed tempts no one; but we pray in this petition that God would guard and keep us, so that the devil, the world, and our flesh may not deceive us nor seduce us into misbelief, despair, and other great shame and vice; and though we be assailed by them, that still we may finally overcome and gain the victory.")

D("2027-01-31",S,"Singing at Midnight","a 3rd–5th grader","Acts 16:25–26",[(25,"About midnight Paul and Silas were praying and singing hymns to God, and the prisoners were listening to them,"),(26,"and suddenly there was a great earthquake, so that the foundations of the prison were shaken. And immediately all the doors were opened, and everyone’s bonds were unfastened.")],
"Paul and Silas in prison",[
"The Seventh Petition is “But deliver us from evil.” It’s like a summary of the whole prayer: we ask our Father to rescue us from everything bad, in body and soul, and when our last hour comes, to take us to Himself in heaven. Then we end with, “For Thine is the kingdom and the power and the glory forever and ever. Amen.”",
"Paul and Silas were traveling to tell people about Jesus. In the city of Philippi, they were beaten and thrown into prison, with their feet locked in wooden stocks. It was dark, and they hurt. But at midnight, Paul and Silas were praying and singing hymns to God, and the other prisoners were listening!",
"Suddenly an earthquake shook the prison. Every door flew open, and everyone’s chains fell off! The jailer was terrified, but Paul said, “Don’t hurt yourself. We’re all here!” The jailer asked, “What must I do to be saved?” They said, “Believe in the Lord Jesus.” That very night, the jailer and his whole family were baptized, and he was filled with joy."],
"Amen",["God delivered Paul and Silas, and He delivers us, sometimes right away, and always in the end. That’s why we can say “Amen,” which means “Yes, yes, it shall be so.” Luther says we can be certain these prayers are heard, because God Himself commanded us to pray and promised to hear us. We’ve now learned the whole Lord’s Prayer!"],
["What were Paul and Silas doing at midnight? What happened next?","What did the jailer ask? What did Paul tell him?","What does “Amen” mean? Why can we be sure God hears our prayers?"],
"Heavenly Father, deliver us from evil. Thank You for rescuing Paul and Silas, and for promising to take us to Yourself in heaven. For Thine is the kingdom and the power and the glory forever and ever.","Help us sing and pray even in hard times, and teach us to say “Amen” with confidence.",
"Paul and Silas sang in prison at midnight. God sent an earthquake, and the doors flew open!",
["Paul and Silas were in [prison].","At midnight they were [singing].","An [earthquake] shook the prison.","The jailer’s whole family was [baptized].","Amen means “Yes, it shall be [so].”"],
["PAUL","SILAS","PRISON","MIDNIGHT","SINGING","AMEN"],[("What were Paul and Silas doing at midnight?",["Singing and praying","Complaining"],0),("What does Amen mean?",["Yes, it shall be so","The end"],0)],
"Draw Paul and Silas singing in prison, with the doors flying open.",("Acts 16:25","“About midnight Paul and Silas were praying and singing hymns to God.”"),
scene(moon(560,50),bars(60,260),person(380,beard=True,arms="up",hair="short",s=.75),person(480,beard=True,arms="up",hair="curly",s=.75),'<path d="M300,300 l20,-30 l-14,-10 l24,-26 M580,300 l-16,-24 l14,-10 l-18,-26" fill="none"/>',label="Coloring picture: Paul and Silas singing in prison"))
ALL[-1]['cat']=dict(part="The Seventh Petition and the Conclusion",text="But deliver us from evil. For Thine is the kingdom and the power and the glory forever and ever. Amen.",mean="We pray in this petition, as the sum of all, that our Father in heaven would deliver us from all manner of evil, of body and soul, property and honor, and finally, when our last hour has come, grant us a blessed end, and graciously take us from this vale of tears to Himself in heaven. Amen means: that I should be certain that these petitions are acceptable to our Father in heaven, and heard; for He Himself has commanded us so to pray, and has promised to hear us.")
