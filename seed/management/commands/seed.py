from django.core.management.base import BaseCommand
import seed.seed as s


class Command(BaseCommand):
    help = 'Populate tables'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando inserção de dados.')

        s.seed_uf()
        self.stdout.write('uf inserido.')

        s.seed_setor()
        self.stdout.write('setor inserido.')

        s.seed_segmento()
        self.stdout.write('segmento inserido.')

        s.seed_tipoIndustria()
        self.stdout.write('tipo industria inserido.')

        s.seed_valorArrecadacao()
        self.stdout.write('valor arrecadacao inserido.')

        s.seed_endereco()
        self.stdout.write('endereco inserido.')

        s.seed_fundamento()
        self.stdout.write('fundamento inserido.')

        s.seed_resposta()
        self.stdout.write('resposta inserida.')

        s.seed_tipo_diagnostico()
        self.stdout.write('tipo diagnostico inserido.')

        # s.seed_pergunta()
        # self.stdout.write('pergunta inserida.')
