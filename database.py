import sqlite3

sights = [
    {'name': 'Этно – мемориальный комплекс «Атамекен»',
     'description': 'Этно-мемориальный комплекс «Карта Казахстана «Атамекен» был открыт 8 сентября 2001 года по инициативе первого Президента Республики Казахстан Н.А.Назарбаева. Учредителем предприятия является акимат города Астаны. Уполномоченным органом предприятия является Управление культуры города Астана.',
     'value': '''Целью деятельности Карты Казахстана «Атамекен» является обеспечение сохранности, доступности и приобщение населения к историко-культурным и духовным ценностям, пропаганда достижений казахстанской культуры, содействие в изучении исторического наследия Казахстана, отражение колоритности всех природных зон и экономических достижений Республики Казахстан, сохранение и приумножение культурных ценностей. Познавательно-художественный комплекс «Карта Казахстана «Атамекен» познакомит Вас с историей государства, культурой народов его населяющих.
Стилизованные горы, возвышенности, степи, леса, озера, символически обозначенные крупнейшие города составляют символический ансамбль этого центра культуры. Интересной частью Карты Казахстана «Атамекен» является декоративно оформленная модель Каспийского моря.''',
     'price':
'''Экскурсия на казахском языке – 200 тенге

Экскурсия на русском языке – 200 тенге

Экскурсия на английском языке – 500 тенге

Фотосъемка – 300 тенге

Участникам и инвалидам ВОВ – вход бесплатный и вне очереди (при предъявлении подтверждающих документов).

Инвалидам I, II группы и детям-инвалидам до 18 лет – вход бесплатный (при предъявлении подтверждающих документов).

Инвалидам III группы – скидка 50% от стоимости входного билета (при предъявлении подтверждающих документов).

Детям-сиротам и детям, оставшимся без попечения родителей, которые не достигли 18 лет – вход бесплатный (при предъявлении подтверждающих документов).

Детям до 5 (пяти) лет – вход бесплатный (при предъявлении подтверждающих документов).''',
     'start': '10:00',
     'end': '19:00',
     'address': ' Астана, Коргалжинское шоссе, 2/1',
     'phone': '+7 (7172) 79-04-39',
     'transport': '№ 32 , 44 , 28'},
    {'name': 'Музей энергии будущего «Нур-Алем» (ЭКСПО)',
     'description': '''“Нур-Алем”- это главный символ выставки ЭКСПО Астана, гигантское сферическое здание, диаметром 80 метров. На вершине шара расположились два ветрогенератора, вырабатывающие энергию, тем самым снижая потребление энергии из сети. Строение состоит из восьми уровней, каждый из которых рассказывает об одном из альтернативных источников энергии – «Энергия космоса», «Энергия Солнца», «Энергия ветра», «Энергия биомасс», «Кинетическая энергия», «Энергия воды». На восьмом уровне расположился музей «Будущая Астана», а основание сферы, площадью 5000 кв. метров занимает национальный павильон. Он разделен на две зоны: знакомство с Казахстаном и «Созидательная энергия». В музее энергии будущего представлены проекты ученых Казахстана и стартап-проекты молодых специалистов в области «зеленых» источников энергии.''',
     'value': '''Несмотря на то, что выставка ЭКСПО закончилась, после небольшой реконструкции территория выставки продолжает пользоваться большой популярностью среди туристов. Теперь цены на билеты значительно ниже, чес в период прохождения выставки.

Большая работа проделана по сохранению наследия ЭКСПО и процветанию идей «Энергии будущего».

Инфраструктура представлена действующим транспортно-логистическим центром, функционирующим, как таможенный терминал, оснащенный складскими помещениями, Центром коммуникаций, включающим в себя центр обработки данных и медиа-центр для цифровых, телевизионных и печатных СМИ, офисом управляющей компании АО «НК «Астана ЭКСПО-2017» и зданием оперативного отдела внутренних дел. На территории ЭКСПО регулярно проводятся экскурсии. ''',
     'price': 'Цена за билеты на ЭКСПО составит 1500 тенге.',
    'start': '10:00',
     'end': '20:00',
     'address': 'Астана, Орынбор , 55.',
     'phone': '+7 (7172) 79-04-39',
     'transport': '№ 504 , 506 , 500 , 502 , 501 , 505'},
    {
        'name': 'Колесо обозрения «Ailand» ',
         'description': '''Колесо обозрения в Астане «Ailand» высотой 65 метров и весом 270 тонн, является самым большим колесом обозрения Казахстана. Это совершенно новый проект, специально разработанный с учетом климатических особенностей Астаны. Подобные технологии используются для строительства аттракционов в зонах торнадо.
    Колесо обозрения оборудовано 36 закрытыми кабинками с панорамным видом на город. В каждой кабинке разместились системы кондиционирования и отопления, что позволит насладиться видами города в любую погоду. Вместимость стандартной кабинки – 6 человек, также имеются четыре кабинки повышенной комфортности. Колесо обозрения «Ailand» работает круглые сутки, а это значит, что Вы можете вдоволь насладиться отличным видом как на дневной, так и ночной город.''',
            'value': '''Еще до своего официального открытия колесо обозрения «Ailand» стало героем известной телепередачи о путешествиях «Орел и Решка. Перезагрузка». Ведущей программы Анастасии Ивлеевой, посчастливилось одной из первых прокатиться на колесе обозрения и взглянуть сверху на молодую, современную, красивую и величественную столицу.
    
    После своего открытия, колесо обозрения стало новой достопримечательностью Астаны и завоевало сердца жителей и гостей города. Прокатившись на колесе обозрения, Вы сможете насладиться отличными видами на столицу с высоты птичьего полета.''',
         'price': 'None',
         'start': '10:00',
         'end': '20:00',
         'address': 'Астана, Коргалжинское шоссе, 2',
         'phone':' +7 (7172) 79-04-39',
         'transport': '№ 12 , 18 , 21 , 27 , 28 , 35 , 42 , 43 , 44'
    },
    {
        'name': 'ТРЦ «Хан Шатыр»',
        'description': '''Этот торгово-развлекательный центр по праву называют новым символом Астаны. Спроектированный знаменитым британским архитектором Норманом Фостером, «Хан Шатыр» является крупнейшим сооружением шатровой формы в мире, и в то же время самым большим торговым центром в Казахстане. Торгово-развлекательный центр был открыт в 2010 году, на день столицы.''',
        'value': '''Здесь размещены рознично-торговые и развлекательные комплексы. В том числе супермаркет, семейный парк, кафе и рестораны, кинотеатры, спортивные залы, аквапарк с искусственным пляжем и бассейны с эффектом волн, служебные и офисные помещения, паркинг на 700 мест и многое другое. Но главная особенность «Хан Шатыра» — пляжный курорт с тропическим климатом, экзотическими растениями и температурой +35 градусов круглый год. Песчаные пляжи курорта оснащены системой отопления, создающей ощущение настоящего пляжа, а песок привезен с Мальдивских островов. Помимо этого, каждые выходные в «Хан Шатыре» проводятся специальные мероприятия; в главном атриуме регулярно проходят лотереи и различные интересные мероприятия.''',
        'price': 'None',
        'start': '10:00',
        'end': '22:00',
        'address': 'ул. Туран 37',
        'phone': '+7 (71727) 79-04-39',
        'transport': '№ 10 12 26'
    },
    {
        'name': 'Театр аниматрониксов «Джунгли»',
        'description': '''Парк динозавров в Астане стал уникальным проектом, не имеющим аналогов в СНГ. В нем удивительным образом сочетаются театральные представления и увлекательное путешествие по недрам джунглей с роботами-динозаврами и катанием на водных горках.

Роботы-аниматрониксы для динопарка были разработаны и созданы в Казахстане, отечественной компанией «Казахстан Салют», главным конструктором машин выступил Вадим Гостев. Этот факт придает еще большей уникальности аттракциону, ведь впервые аниматрониксы создавались на территории Республики.

Парк аниматрониксов «Джунгли» предлагает Вам окунуться в атмосферу непроходимых джунглей и прогуляться среди огромных доисторических животных. Динопарк в Астане стал крупнейшим проектом Республики, воссоздавший в себе всю красоту и таинственность джунглей. Захватывающие приключения в затерянном мире, которые Вы могли наблюдать в голливудских фильмах, теперь доступны абсолютно всем. Таинственный мир джунглей очарует и увлечет Вас с первых минут. Опытные гиды и аниматоры проведут для Вас веселую, интересную и познавательную экскурсию в загадочный парк динозавров, с его доисторическими обитателями, попутно рассказывая истории, пришедшие к нам с древних времен.

Динозавры, трицерапторы, тираннозавры, первобытные племена – вся атмосфера динопарка пропитана волнительным духом джунглей, погрузившись в которую Вы забудете обо все на свете, и поверите, что представленная реальность действительна.

Расположившись в здании РЦ «Ailand», динопарк занимает более 3000 м2 площади, которая густо заселена различными обитателями флоры и фауны диких джунглей.

На входе в театр аниматрониксов Вас встретит огромное каменное лицо древнего божества, которое оживет на Ваших глазах и, завораживая своим магическим взглядом, уведет Вас в заросли джунглей. Пройдя в образовавшуюся щель, Вы окажитесь в настоящей пещере. Здесь Вас встретит огромный паук с множеством гигантских и мохнатых лап, который не упустит возможности Вас напугать, вокруг него уже собралось множество маленьких пауков, они вот-вот поползут па Вам. Пройдя дальше, Вы наткнетесь на двух огромных 5-ти метровых крокодила, ждущих свою добычу на берегу реки. Пройдет по мостику Вы наткнетесь на гигантских лягушек и мифического Горгония, весело отплясывающих под зажигательную музыку.''',
        'value': 'Идея создания единственного в своем роде парка динозавров принадлежала президенту РК Н.А. Назарбаеву. Открытие динопарка состоялось 6 июля 2008 года – в День столицы (Астаны), именно в этот праздничный день «Джунгли» впервые открыли свои двери для посетителей.',
        'price': 'Приобретая Astana Pass (24 или 72 часовой), Вы можете посетить эту достопримечательность и 11 других достопримечательностей и 2 экскурсии города, абсолютно БЕСПЛАТНО. В течение действия онлайн-карты.',
        'start': '10:00',
        'end': '20:00',
        'address': ' г. Астана, Коргалжинское шоссе, 2',
        'phone': '+7 (7172) 79-04-39',
        'transport': '№ 12 , 18 , 21 , 27 , 28 , 35 , 42 , 43 , 44 '
    },
    {
        'name': 'Дворец Мира и Согласия',
        'description': '''В выставочных залах организуются временные выставки, творческие встречи, на которых собираются художники Казахстана и других стран.

На верху пирамиды расположился зал «Колыбель», принимающий гостей II всемирно значимого съезда мировых и традиционно-национальных религий. Для того что бы подняться на самый верх пирамиды можно воспользоваться панорамными лифтами, которые движутся не вертикально, а по диагонали. Во время движения Вы можете насладиться прекрасными террасами, живописно украшенными зеленью. Так же можно совершить пеший подъем по лестницам, проходящим сквозь чарующие висячие сады, состоящие из растений, завезенных с разных уголков Земли.

Пирамида Астаны притягивает посетителей красотой здания, интересными решениями внутреннего интерьера и уютной парковой зоной вокруг. Ночью, когда витражная вершина пирамиды подсвечивается изнутри, здание становится видимым практически из любой точки столицы.

Дворец Мира и Согласия стал символом единения культур для жителей столицы и всей Республики Казахстан.''',
        'value': 'Город Астана может похвастаться множеством впечатляющих мест, которые появились здесь с момента объявления столицей. Одной из узнаваемых достопримечательностей города стал Дворец Мира и Согласия. Это единственное здание в форме пирамиды, считающееся еще одним чудом света. Идея возведения Дворца Мира и Согласия принадлежит Первому Президенту Республики Казахстан –  Нурсултану Назарбаеву, предложившему возвести этот смелый объект, предназначенный для съездов представителей мировых религий.',
        'price': 'None',
        'start': '10:00',
        'end': '18:00 ',
        'address': 'Астана, проспект Тауелсiздiк 57',
        'phone': '+7 (7172) 79-04-39',
        'transport': '№ 4 , 14 , 19 , 21 , 29 , 40 '
    },
    {
        'name': 'Монумент «Астана-Байтерек»',
        'description': 'Монумент «Байтерек» является одной из главных достопримечательностей столицы, которую должен посетить каждый турист, поэтому ежедневно на вершину монумента поднимается множество туристов, порой создавая очереди за покупкой билетов в кассе. В среднем за год Байтерек посещает около 500 тысяч туристов.',
        'value': 'Байтерек – это символ независимого Казахстана, главная достопримечательность нашей столицы. В связи с этим поток желающих посетить Байтерек не уменьшается, и возникают очереди. Со онлайн-картой Astana PASS Вы минуете очередь на кассе, но к сожалению должны ожидать в живой очереди.',
        'price': 'Для взрослых стоимость билета в Монумент составляет 700 тенге, цена для детей 300 тенге.',
        'start': '09:00',
        'end': '21:00',
        'address': 'Астана, Нуржол бульвар, 14',
        'phone': '+7 (7172) 79-04-39',
        'transport': '№ 14 , 21 , 28 , 46'
    },
    {
        'name': 'Океанариум «Ailand»',
        'description': 'Океанариум города Астана, развлекательного центра «Ailand» (бывший “Думан”) – частичка бескрайнего океана в самом центре засушливой степной зоны. Океанариум до сих пор остается первым и единственным в своем роде в Казахстане и по праву считается самым отдаленным от океана во всем мире. Удаленность от ближайшего океана составляет более 3000 км. Благодаря этой особенности океанариум занесен в книгу Рекордов Гиннеса.',
        'value': 'Удивительный казахстанский океанариум в Астане открылся в далеком 2003 году и сразу покорил сердца посетителей своей масштабностью и захватывающим зрелищем. Огромные резервуары вмещают в себя 3 млн. л. воды и 120 тонн морской соли и создают естественные условия для комфортного проживания морских обитателей.',
        'price': 'Цена билета в океанариум со смарт-картой Astana PASS станет еще выгоднее. Cо онлайн-картой Astana PASS Вы проходите сразу к турникету океанариума.',
        'start': ' 10:00',
        'end': '20:00',
        'address': 'Астана, Коргалжинское шоссе, 2',
        'phone': '+7 (7172) 79-04-39',
        'transport': '№ 12 , 18 , 21 , 27 , 28 , 35 , 42 , 43 , 44'
    },
    {
        'name': 'Экзотариум «Ailand»',
        'description': '''В экзотариуме царит особая атмосфера: затемненное помещение, приятная прохлада от работающих кондиционеров, декорированные стены и потолок. Здесь располагаются всевозможные террариумы, переходя от одного к другому, можно познакомиться с экзотическим животным, последить за его повадками и поведением.

Крокодилы, питоны, пауки, обезьяны и другие ждут Вас и Вашу семью в Экзотариуме!''',
        'value': 'Один из уголков Центра семейного отдыха «Ailand» таит в себе загадочных и экзотических животных. Они приехали в Астану из разных точек мира. Рептилии, земноводные, хищные и травоядные млекопитающие проживают теперь в специально созданных условиях, приближенные к их естественной среде обитания.',
        'price': 'None',
        'start': '10:00',
        'end': '20:00',
        'address': 'Астана, Коргалжинское шоссе, 2',
        'phone': '+7 (7172) 79-04-39',
        'transport': '№ 12 , 18 , 21 , 28 , 32 , 43 , 44'
    }
]




with  sqlite3.connect('db.sqlite') as connection :
    cursor = connection.cursor()
    for sight in sights:
        cursor.execute(f"INSERT INTO places (name, description, value, price, start, end, address, phone, transport) VALUES ('{sight['name']}', '{sight['description']}', '{sight['value']}', '{sight['price']}', '{sight['start']}', '{sight['end']}', '{sight['address']}', '{sight['phone']}', '{sight['transport']}')")
    
    cursor.close()
