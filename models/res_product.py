# -*- coding: utf-8 -*-
# Part of eagle. See LICENSE file for full copyright and licensing details.

from odoo import _,fields, models,api

class productBook(models.Model):
    _inherit = 'product.template'
    is_book=fields.Boolean("Is A Book",default=False)
    publisher_id=fields.Many2one("res.partner",string="Publisher")
    writer_ids=fields.Many2many("res.partner",'partner_product_template_rel','written','writer_ids',string="Writer")
    prefix = fields.Char("Prefix")
    suffix = fields.Char("Suffix")
    def name_get(self):
        result = []

        for record in self:
            string = ""
            if  len(record.writer_ids)>0:
                for rec in record.writer_ids:
                    if not rec.nick:
                        rec.nick=""
                    string= string+ " " + rec.nick

            record_name = record.name + string
            result.append((record.id, record_name))
        return result


class product_product(models.Model):
    _inherit = "product.product"

    pricelist_item_ids = fields.One2many(
        'product.pricelist.item','product_id',string='Pricelist Items')
    product_price_list_item_count = fields.Integer(
        '# Pricelist', compute='_compute_product_pricelist_items_count')




    def _compute_product_pricelist_items_count(self):
        self.product_price_list_item_count = len(self.with_prefetch().pricelist_item_ids)


