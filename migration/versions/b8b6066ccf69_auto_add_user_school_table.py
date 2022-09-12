"""Auto_add_user_school_table

Revision ID: b8b6066ccf69
Revises: 
Create Date: 2022-09-08 14:22:23.069745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b6066ccf69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('SchoolProfile',
    *[sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('post', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('ctv', sa.String(), nullable=True),
    sa.Column('pincode', sa.BigInteger(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('mobile', sa.BigInteger(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('needs', sa.String(), nullable=True),
    sa.Column('academic', sa.String(), nullable=True),
    sa.Column('establish', sa.String(), nullable=True),
    sa.Column('level', (sa.ARRAY(sa.String())), nullable=True),
    sa.Column('medium', sa.String(), nullable=True),
    sa.Column('affiliation', sa.String(), nullable=True),
    sa.Column('t_staff', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('girl', sa.Integer(), nullable=True),
    sa.Column('boys', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('n_staff', sa.Integer(), nullable=True),
    sa.Column('correspondent_name', sa.String(), nullable=True),
    sa.Column('correspondent_mobile', sa.BigInteger(), nullable=True),
    sa.Column('correspondent_mail', sa.String(), nullable=True),
    sa.Column('principal_name', sa.String(), nullable=True),
    sa.Column('principal_mail', sa.String(), nullable=True),
    sa.Column('principal_office_mobile', sa.BigInteger(), nullable=True),
    sa.Column('principal_mobile', sa.BigInteger(), nullable=True),
    sa.Column('recognized', sa.String(), nullable=True),
    sa.Column('board_name', sa.String(), nullable=True),
    sa.Column('affiliate_number', sa.String(), nullable=True),
    sa.Column('affiliate_year', sa.Integer(), nullable=True),
    sa.Column('affiliate_type', sa.String(), nullable=True),
    sa.Column('affiliate_state', sa.String(), nullable=True),
    sa.Column('christian', sa.Integer(), nullable=True),
    sa.Column('hindu', sa.Integer(), nullable=True),
    sa.Column('islam', sa.Integer(), nullable=True),
    sa.Column('others', sa.Integer(), nullable=True),
    sa.Column('nonBeliver', sa.Integer(), nullable=True),
    sa.Column('fire', sa.String(), nullable=True),
    sa.Column('sanitation', sa.String(), nullable=True),
    sa.Column('building', sa.String(), nullable=True),
    sa.Column('minority', sa.String(), nullable=True),
    sa.Column('own', sa.String(), nullable=True),
    sa.Column('trust_name', sa.String(), nullable=True),
    sa.Column('trust_register', sa.String(), nullable=True),
    sa.Column('register_act', sa.String(), nullable=True),
    sa.Column('register_year', sa.Integer(), nullable=True),
    sa.Column('register_no', sa.String(), nullable=True),
    sa.Column('register_validity', sa.Integer(), nullable=True),
    sa.Column('president_name', sa.String(), nullable=True),
    sa.Column('president_designation', sa.String(), nullable=True),
    sa.Column('president_address', sa.String(), nullable=True),
    sa.Column('president_number', sa.BigInteger(), nullable=True),
    sa.Column('president_email', sa.String(), nullable=True),
    sa.Column('gover_trust', sa.String(), nullable=True),
    sa.Column('gover_member', sa.Integer(), nullable=True),
    sa.Column('gover_tenure', sa.Integer(), nullable=True),
    sa.Column('educative', sa.String(), nullable=True),
    sa.Column('educative_member', sa.Integer(), nullable=True),
    sa.Column('educative_tenure', sa.Integer(), nullable=True),
    sa.Column('pta', sa.String(), nullable=True),
    sa.Column('pta_member', sa.Integer(), nullable=True),
    sa.Column('pta_tenure', sa.Integer(), nullable=True),
    sa.Column('student_council', sa.String(), nullable=True),
    sa.Column('student_member', sa.Integer(), nullable=True),
    sa.Column('student_tenure', sa.Integer(), nullable=True),
    sa.Column('general_complaint', sa.String(), nullable=True),
    sa.Column('school_commit', sa.String(), nullable=True),
    sa.Column('constitution_commit', sa.String(), nullable=True),
    sa.Column('constitution_member', sa.Integer(), nullable=True),
    sa.Column('constitution_tenure', sa.Integer(), nullable=True),
    sa.Column('school_building', sa.String(), nullable=True),
    sa.Column('schoolArea', sa.String(), nullable=True),
    sa.Column('schoolBuilt', sa.String(), nullable=True),
    sa.Column('groundArea', sa.String(), nullable=True),
    sa.Column('noBuilding', sa.Integer(), nullable=True),
    sa.Column('provision', sa.Integer(), nullable=True),
    sa.Column('noStaircase', sa.Integer(), nullable=True),
    sa.Column('lift', sa.Integer(), nullable=True),
    sa.Column('classRoom', sa.Integer(), nullable=True),
    sa.Column('staffRoom', sa.Integer(), nullable=True),
    sa.Column('physicalLab', sa.Integer(), nullable=True),
    sa.Column('chemistryLab', sa.Integer(), nullable=True),
    sa.Column('biologylab', sa.Integer(), nullable=True),
    sa.Column('mathsLab', sa.Integer(), nullable=True),
    sa.Column('science', sa.Integer(), nullable=True),
    sa.Column('library', sa.Integer(), nullable=True),
    sa.Column('auditorium', sa.Integer(), nullable=True),
    sa.Column('counselor', sa.Integer(), nullable=True),
    sa.Column('parlor', sa.Integer(), nullable=True),
    sa.Column('prayer', sa.Integer(), nullable=True),
    sa.Column('sick', sa.Integer(), nullable=True),
    sa.Column('canteen', sa.Integer(), nullable=True),
    sa.Column('security', sa.Integer(), nullable=True),
    sa.Column('otherRoom', sa.Integer(), nullable=True),
    sa.Column('staffToilets', sa.Integer(), nullable=True),
    sa.Column('studToilet', sa.Integer(), nullable=True),
    sa.Column('teacher', sa.String(), nullable=True),
    sa.Column('boundry', sa.String(), nullable=True),
    sa.Column('boundry_wall', sa.String(), nullable=True),
    sa.Column('cctv', sa.String(), nullable=True),
    sa.Column('dataSave', sa.String(), nullable=True),
    sa.Column('camera', sa.Integer(), nullable=True),
    sa.Column('maleGuard', sa.String(), nullable=True),
    sa.Column('noMaleGuard', sa.Integer(), nullable=True),
    sa.Column('femaleGuard', sa.String(), nullable=True),
    sa.Column('noFemaleGuard', sa.Integer(), nullable=True),
    sa.Column('drinkWater', sa.String(), nullable=True),
    sa.Column('drainage', sa.String(), nullable=True),
    sa.Column('midday', sa.String(), nullable=True),
    sa.Column('nobus', sa.Integer(), nullable=True),
    sa.Column('gps', sa.Integer(), nullable=True),
    sa.Column('noladyAttend', sa.Integer(), nullable=True),
    sa.Column('firstAid', sa.Integer(), nullable=True),
    sa.Column('noDrinkWater', sa.Integer(), nullable=True),
    sa.Column('BusContract', sa.Integer(), nullable=True),
    sa.Column('buspass', sa.String(), nullable=True),
    sa.Column('freeTransport', sa.String(), nullable=True),
    sa.Column('library_open', sa.TIME(), nullable=True),
    sa.Column('library_close', sa.TIME(), nullable=True),
    sa.Column('noBook', sa.Integer(), nullable=True),
    sa.Column('magazine', sa.Integer(), nullable=True),
    sa.Column('noNews', sa.Integer(), nullable=True),
    sa.Column('noEbook', sa.Integer(), nullable=True),
    sa.Column('primaryLibrary', sa.String(), nullable=True),
    sa.Column('remedial', sa.String(), nullable=True),
    sa.Column('tv', sa.Boolean(), nullable=True),
    sa.Column('digitalboard', sa.Boolean(), nullable=True),
    sa.Column('computer', sa.Boolean(), nullable=True),
    sa.Column('projector', sa.Boolean(), nullable=True),
    sa.Column('tape', sa.Boolean(), nullable=True),
    sa.Column('ppm', sa.Integer(), nullable=True),
    sa.Column('ppf', sa.Integer(), nullable=True),
    sa.Column('tpm', sa.Integer(), nullable=True),
    sa.Column('tpf', sa.Integer(), nullable=True),
    sa.Column('pvm', sa.Integer(), nullable=True),
    sa.Column('pvf', sa.Integer(), nullable=True),
    sa.Column('tvm', sa.Integer(), nullable=True),
    sa.Column('tvf', sa.Integer(), nullable=True),
    sa.Column('ppgtm', sa.Integer(), nullable=True),
    sa.Column('ppgtf', sa.Integer(), nullable=True),
    sa.Column('tpgtm', sa.Integer(), nullable=True),
    sa.Column('tpgtf', sa.Integer(), nullable=True),
    sa.Column('ptgtm', sa.Integer(), nullable=True),
    sa.Column('ptgtf', sa.Integer(), nullable=True),
    sa.Column('ttgtm', sa.Integer(), nullable=True),
    sa.Column('ttgtf', sa.Integer(), nullable=True),
    sa.Column('pprtm', sa.Integer(), nullable=True),
    sa.Column('pprtf', sa.Integer(), nullable=True),
    sa.Column('tprtm', sa.Integer(), nullable=True),
    sa.Column('tprtf', sa.Integer(), nullable=True),
    sa.Column('pnttm', sa.Integer(), nullable=True),
    sa.Column('pnttf', sa.Integer(), nullable=True),
    sa.Column('tnttm', sa.Integer(), nullable=True),
    sa.Column('tnttf', sa.Integer(), nullable=True),
    sa.Column('putm', sa.Integer(), nullable=True),
    sa.Column('putf', sa.Integer(), nullable=True),
    sa.Column('tutm', sa.Integer(), nullable=True),
    sa.Column('tutf', sa.Integer(), nullable=True),
    sa.Column('plm', sa.Integer(), nullable=True),
    sa.Column('plf', sa.Integer(), nullable=True),
    sa.Column('tlm', sa.Integer(), nullable=True),
    sa.Column('tlf', sa.Integer(), nullable=True),
    sa.Column('pmtm', sa.Integer(), nullable=True),
    sa.Column('pmtf', sa.Integer(), nullable=True),
    sa.Column('tmtm', sa.Integer(), nullable=True),
    sa.Column('tmtf', sa.Integer(), nullable=True),
    sa.Column('pctm', sa.Integer(), nullable=True),
    sa.Column('pctf', sa.Integer(), nullable=True),
    sa.Column('tctm', sa.Integer(), nullable=True),
    sa.Column('tctf', sa.Integer(), nullable=True),
    sa.Column('pcltm', sa.Integer(), nullable=True),
    sa.Column('pcltf', sa.Integer(), nullable=True),
    sa.Column('tcltm', sa.Integer(), nullable=True),
    sa.Column('tcltf', sa.Integer(), nullable=True),
    sa.Column('pfmm', sa.Integer(), nullable=True),
    sa.Column('pfmf', sa.Integer(), nullable=True),
    sa.Column('tfmm', sa.Integer(), nullable=True),
    sa.Column('tfmf', sa.Integer(), nullable=True),
    sa.Column('pnm', sa.Integer(), nullable=True),
    sa.Column('pnf', sa.Integer(), nullable=True),
    sa.Column('tnm', sa.Integer(), nullable=True),
    sa.Column('tnf', sa.Integer(), nullable=True),
    sa.Column('pptm', sa.Integer(), nullable=True),
    sa.Column('pptf', sa.Integer(), nullable=True),
    sa.Column('tptm', sa.Integer(), nullable=True),
    sa.Column('tptf', sa.Integer(), nullable=True),
    sa.Column('pom', sa.Integer(), nullable=True),
    sa.Column('tom', sa.Integer(), nullable=True),
    sa.Column('ptom', sa.Integer(), nullable=True),
    sa.Column('poa', sa.Integer(), nullable=True),
    sa.Column('toa', sa.Integer(), nullable=True),
    sa.Column('ptoa', sa.Integer(), nullable=True),
    sa.Column('pc', sa.Integer(), nullable=True),
    sa.Column('tc', sa.Integer(), nullable=True),
    sa.Column('ptc', sa.Integer(), nullable=True),
    sa.Column('pla', sa.Integer(), nullable=True),
    sa.Column('tla', sa.Integer(), nullable=True),
    sa.Column('ptla', sa.Integer(), nullable=True),
    sa.Column('pa', sa.Integer(), nullable=True),
    sa.Column('ta', sa.Integer(), nullable=True),
    sa.Column('ptac', sa.Integer(), nullable=True),
    sa.Column('ppc', sa.Integer(), nullable=True),
    sa.Column('tpc', sa.Integer(), nullable=True),
    sa.Column('ptpc', sa.Integer(), nullable=True),
    sa.Column('po', sa.Integer(), nullable=True),
    sa.Column('to', sa.Integer(), nullable=True),
    sa.Column('pto', sa.Integer(), nullable=True),
    sa.Column('no_of_act', sa.Integer(), nullable=True),
    sa.Column('no_of_group', sa.Integer(), nullable=True),
    sa.Column('no_of_service', sa.Integer(), nullable=True),
    sa.Column('school_sports', sa.Integer(), nullable=True),
    sa.Column('zonal_sports', sa.Integer(), nullable=True),
    sa.Column('district_sports', sa.Integer(), nullable=True),
    sa.Column('state_sports', sa.Integer(), nullable=True),
    sa.Column('national_sports', sa.Integer(), nullable=True),
    sa.Column('international_sports', sa.Integer(), nullable=True),
    sa.Column('school_compet', sa.Integer(), nullable=True),
    sa.Column('zonal_compet', sa.Integer(), nullable=True),
    sa.Column('district_compet', sa.Integer(), nullable=True),
    sa.Column('state_compet', sa.Integer(), nullable=True),
    sa.Column('national_compet', sa.Integer(), nullable=True),
    sa.Column('international_compet', sa.Integer(), nullable=True),
    sa.Column('school_program', sa.Integer(), nullable=True),
    sa.Column('zonal_program', sa.Integer(), nullable=True),
    sa.Column('district_program', sa.Integer(), nullable=True),
    sa.Column('state_program', sa.Integer(), nullable=True),
    sa.Column('national_program', sa.Integer(), nullable=True),
    sa.Column('international_program', sa.Integer(), nullable=True),
    sa.Column('school_history', sa.String(), nullable=True),
    sa.Column('school_plan', sa.String(), nullable=True),
    sa.Column('academic_begin_month', sa.String(), nullable=True),
    sa.Column('academic_end_month', sa.String(), nullable=True),
    sa.Column('no_of_work_2021', sa.Integer(), nullable=True),
    sa.Column('no_of_work_2020', sa.Integer(), nullable=True),
    sa.Column('no_of_work_2019', sa.Integer(), nullable=True),
    sa.Column('no_of_hour_2021', sa.Integer(), nullable=True),
    sa.Column('no_of_hour_2020', sa.Integer(), nullable=True),
    sa.Column('no_of_hour_2019', sa.Integer(), nullable=True),
    sa.Column('no_of_totalhour_2021', sa.Integer(), nullable=True),
    sa.Column('no_of_totalhour_2020', sa.Integer(), nullable=True),
    sa.Column('no_of_totalhour_2019', sa.Integer(), nullable=True),
    sa.Column('no_of_dayStaff_2021', sa.Integer(), nullable=True),
    sa.Column('no_of_dayStaff_2020', sa.Integer(), nullable=True),
    sa.Column('no_of_dayStaff_2019', sa.Integer(), nullable=True),
    sa.Column('no_of_holiday_2021', sa.Integer(), nullable=True),
    sa.Column('no_of_holiday_2020', sa.Integer(), nullable=True),
    sa.Column('no_of_holiday_2019', sa.Integer(), nullable=True),
    sa.Column('no_of_subject', sa.Integer(), nullable=True),
    sa.Column('no_of_moral', sa.Integer(), nullable=True),
    sa.Column('teach_time', sa.Integer(), nullable=True),
    sa.Column('no_of_activity', sa.Integer(), nullable=True),
    sa.Column('from_summer_time', sa.TIME(), nullable=True),
    sa.Column('to_summer_time', sa.TIME(), nullable=True),
    sa.Column('from_winter_time', sa.TIME(), nullable=True),
    sa.Column('to_winter_time', sa.TIME(), nullable=True),
    sa.Column('school_shift', sa.String(), nullable=True),
    sa.Column('scholarship', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('shift', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('schoolClass', sa.ARRAY(sa.String()), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_data.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('SchoolProfile')
    op.drop_table('user_data')
    # ### end Alembic commands ###