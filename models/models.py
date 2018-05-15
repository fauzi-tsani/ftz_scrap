# -*- coding: utf-8 -*-

from odoo import models, fields, api
import scrappy
class ftz_scrap_scrap_setting(models.Model):
    _name = 'ftz_scrap.scrap_setting'

    name = fields.Char()
    website = fields.Selection({'jakmall':'https://www.jakmall.com/'},string="Target",default='jakmall',required=True,)
    website_filter_ids = fields.One2many(
        'ftz_scrap.scrap_setting_website_filter',
        'scrap_setting_id',
        string='Filter',
    )
    state = fields.Selection(
		[
			('draft', 'Draft'),
			('scraped', 'Scraped'),
			('transfered', 'Transfered'),
		], 
		default='draft')

    scrap_data_ids = fields.One2many(
        'ftz_scrap.scrap_data',
        'scrap_setting_id',
        string='Scrap Data',
    )

    @api.onchange('website')
    def _onchange_website(self):
    	# set default isi website filter berdasarkan isi website
    	pass
    
    @api.one
    def do_scrap(self):
    	# lakukan scrap berdasarkan setting yang di isi
    	# ubah state ke scraped
    	pass


    @api.one
    def do_transfer(self):
    	# lakukan transfer data ke product berdasarkan data yang telah di scrap
    	# ubah state ke transfered
    	pass
class ftz_scrap_scrap_setting_website_filter(models.Model):
    _name = 'ftz_scrap.scrap_setting_website_filter'

    name = fields.Char(
    	string='Name',
    	# size=64,
    	required=False,
    	readonly=False,
    	# defaults={:False}
    	)
    value = fields.Char(
        string='Value',
    )
   	scrap_setting_id = fields.Many2one(
   	    'ftz_scrap.scrap_setting',
   	    string='Scrap Setting',
   	)

class ftz_scrap_scrap_data(models.Model):
    _name = 'ftz_scrap.scrap_data'
    # _description = 'Description'

    scrap_setting_id = fields.Many2one(
   	    'ftz_scrap.scrap_setting',
   	    string='Scrap Setting',
   	)
   	data_website = fields.Char(related="scrap_setting_id.website",
   	    string='Website',
   	    readonly=True, 
   	    store=True,
   	)
    name = fields.Char(
    	string='',
    	required=False,
    	readonly=False,
    	)

	sold = fields.Char(
	    string='sold',
	)
	rating = fields.Char(
	    string='rating',
	)
	weight = fields.Char(
	    string='weight',
	)
	created_at = fields.Char(
	    string='created_at',
	)
	code = fields.Char(
	    string='code',
	)
	sku = fields.Char(
	    string='sku',
	)
	price = fields.Char(
	    string='price',
	)
	final_price = fields.Char(
	    string='final_price',
	)
	discount = fields.Char(
	    string='discount',
	)
	discount_percentage = fields.Char(
	    string='discount_percentage',
	)
	url = fields.Char(
	    string='url',
	)
	image = fields.Char(
	    string='image',
	)
	in_stock = fields.Char(
	    string='in_stock',
	)
	limited_stock = fields.Char(
	    string='limited_stock',
	)
	store = fields.Char(
	    string='store',
	)
	store_image = fields.Char(
	    string='store_image',
	)
	store_url = fields.Char(
	    string='store_url',
	)