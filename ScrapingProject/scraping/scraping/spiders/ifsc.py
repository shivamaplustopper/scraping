import scrapy


class Ifsc(scrapy.Spider):
    name = 'bang'
    start_urls = [
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/akkiramapura-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/aralaguppe-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/beladhara-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/bidare-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/brahmasandra-gate-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/chennakeshavapura-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/chickpet-tmk-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/chikkanayakanahally-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/chikkathotlukere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/chowdanakuppe-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/d-kymara-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/doddahulikunte-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/doddayennegere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/garani-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/gokula-extn-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/gubbi-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/hanumanthapura-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/heggere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/honnavalli-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/hosakere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/hoyisalakatte-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/hullekere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/hunasegatta-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/jayachamarajapura-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/k-palasandra-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kallur-cross-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kandikere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kesarmadu-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kodigenahally-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kolala-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kondajji-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kondethimmanahally-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kora-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/koratagere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/kunigal-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/madhugiri-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/mallasandra-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/manchalakuppe-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/mathigatta-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/mavinahally-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/melekote-road-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/mgroad-tumkur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/midageshi-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/muganayakanakote-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nagalamadike-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nagavalli-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nidasale-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nittur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nonavinakere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/nyayadakunte-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/pavagada-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/prashanthnagara-tumakur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/rantvalalu-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/santhemavathur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/sira-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/sirivara-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/sspuram-tumakuru-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/theerthapura-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/theetha-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/thovinakere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/thumbadi-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/tiptur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/turuvekere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/uridigere-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/uthridurga-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/y-n-hosakote-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/yediyur-branch/',
        'https://banksifsccode.com/kaveri-grameena-bank-ifsc-code/karnataka/tumakuru/yelanadu-branch/',
    ]

    def parse(self, response):
        for bank_name in response.css("tr:nth-child(1) td+ td p strong::text").extract():
            for branch_name in response.css("tr:nth-child(2) td+ td p strong::text").extract():
                for ifsc_code in response.css("tr:nth-child(3) td+ td p a strong::text").extract():
                    for state in response.css("tr:nth-child(4) td+ td p::text").extract():
                        for district in response.css("tr:nth-child(5) td+ td p::text").extract():
                            for city in response.css("tr:nth-child(6) td+ td p::text").extract():
                                for branch_code in response.css("tr:nth-child(7) td+ td p::text").extract():
                                    for address in response.css("tr:nth-child(8) td+ td div p::text").extract():
                                        for phone_no in response.css("tr:nth-child(9) td+ td p::text").extract():
                                            yield {
                                                'bank_name': bank_name,
                                                'branch_name': branch_name,
                                                'ifsc_code': ifsc_code,
                                                'state': state,
                                                'district': district,
                                                'city': city,
                                                'branch_code': branch_code,
                                                'address': address,
                                                'phone_no': phone_no
                                            }


