from openerp import models, fields, api
class DevRequest(models.Model):
    _name = 'dev.request'
    dreqid = fields.Id('Id')
    name = fields.Char('Titulo:', required=True)
    description = fields.Char('Descripcion:', required=True)
    active = fields.Boolean('Sigue pendiente:', default=True)
    date_creation= fields.Date('Solicitado:')
    date_release = fields.Date('Entrega:')

    client_id = fields.Many2one('res.partner','Cliente:')
    task_ids = fields.One2many('dev.request.task','devreq_id')

class DevTask(models.Model):
       _name = 'dev.request.task' 
       name = fields.Char('Descripcion:', required=True)
       devreq_id = fields.Many2one('dev.request','Solicitud:',ondelete='cascade')
       id_done = fields.Boolean('Realizada:',default=False)
       user_id = fields.Many2one('res.users','Responsable:')
       date_deadline = fields.Date('Plazo:')
       horas = fields.Integer('Horas:')
       priority = fields.Selection([
                                    ('0','Baja'),
                                    ('1','Normal'),
                                    ('2','Alta')],
                                    'Prioridad:',default='1')
       kanban_state = fields.Selection([
                                        ('normal', 'Por hacer'),
                                        ('blocked', 'En desarrollo'),
                                        ('done', 'Finalizada')],
                                        'Estado:', default='normal')