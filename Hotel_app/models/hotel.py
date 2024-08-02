from odoo import models,fields,api


class HotelManagement(models.Model):
    _name = 'customer.model'
    _description = 'Hotel management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_name = fields.Char(string='customer name')
    customer_id = fields.Char(string='customer id')
    customer_number = fields.Char(string='customer number',tracking=1)
    customer_address = fields.Char(string=' customer address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'gender')

    _sql_constraints = [
         ('customer_id_uniq', 'unique (customer_id)', "Tag ID already exists !"),
    ]

class RoomManagement(models.Model):
    _name = 'room.model'
    _description = 'Room management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    room_number = fields.Integer(string='room number',tracking=1)
    beds_number = fields.Integer(string='beds number')
    floor_number = fields.Integer(string='floor number')
    room_type = fields.Char(string='room type')


    _sql_constraints = [
    ('room_number_uniq', 'unique (room_number)', "Tag Room Number already exists !"),
    ]

class Booking(models.Model):
    _name = 'booking.model'
    _description = 'Booking management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    booking_id = fields.Integer(string='booking id',tracking=1)
    date_from = fields.Date(string='date from')
    date_to = fields.Date(string='date to')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='draft')


    _sql_constraints = [
        ('booking_id_uniq', 'unique (booking_id)', "Tag ID already exists !"),
    ]










