import scrapy


class Ifsc(scrapy.Spider):
    name = 'micr'
    start_urls = [
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/dholaka-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/ellisbridge-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/ghatlodiya-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/madhupura-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/manekchowk-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/mithakhali-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/odhav-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/raipur-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/thaltej-branch/',
        'https://banksifsccode.com/abhyudaya-co-op-bank-ltd-ifsc-code/gujarat/ahmedabad/vatva-branch/',
    ]

    '''Micr Code'''
    def parse(self, response):
        blank = " "
        for bank_name in response.css("tr:nth-child(1) strong::text").extract():
            for branch_name in response.css("tr:nth-child(2) td+ td p strong::text").extract():
                for ifsc_code in response.css("tr:nth-child(3) td+ td p a strong::text").extract():
                    for micr_code in response.css("tr:nth-child(4) td+ td p a::text").extract():
                        for state in response.css("tr:nth-child(5) td+ td p::text").extract():
                            for district in response.css("tr:nth-child(6) td+ td p::text").extract():
                                for city in response.css("tr:nth-child(7) td+ td p::text").extract():
                                    for branch_code in response.css("tr:nth-child(8) td+ td p::text").extract():
                                        for address in response.css("tr:nth-child(9) td+ td div p::text").extract():
                                            for phone_no in response.css("tr:nth-child(10) td+ td p::text").extract():
                                                yield {
                                                    'bank_name': bank_name,
                                                    'branch_name': branch_name,
                                                    'ifsc_code': ifsc_code,
                                                    'micr_code':micr_code,
                                                    'state': state,
                                                    'district': district,
                                                    'city': city,
                                                    'branch_code': branch_code,
                                                    'address': address,
                                                    'phone_no': phone_no
                                            }


