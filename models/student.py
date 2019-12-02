from odoo import models, fields, api

class StudentStudent(models.Model):
	_name = 'student.student'
	_inherit = 'mail.thread'

	name = fields.Char(string='Name', required=True , track_visibilty='always')
	age = fields.Integer(string='Age', track_visibilty='onchange')
	photo = fields.Binary(string='Image')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Date of Birth")
	student_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')

	nationality = fields.Many2one('res.country', string='Nationality')
	status = fields.Selection([
        ('draft','Draft'),
        ('done','Done'),
        ('cancel','Cancelled')
    ],required=True,default='draft')

	@api.multi
	def button_done(self):
		for rec in self:
			rec.write({'status': 'done'})


