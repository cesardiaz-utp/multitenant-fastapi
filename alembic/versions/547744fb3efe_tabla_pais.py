"""Tabla pais

Revision ID: 547744fb3efe
Revises: ddf285307443
Create Date: 2025-04-01 07:33:56.102995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '547744fb3efe'
down_revision: Union[str, None] = 'ddf285307443'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    """Upgrade schema."""
    # globals()["upgrade_%s" % engine_name]()
    upgrade_engine1()


def downgrade(engine_name: str) -> None:
    """Downgrade schema."""
    # globals()["downgrade_%s" % engine_name]()
    downgrade_engine1





def upgrade_engine1() -> None:
    """Upgrade engine1 schema."""
    op.execute(
        """
        CREATE TABLE ge_pais (
            pais_id bigserial NOT NULL,
            nombre_es varchar(200) NOT NULL,
            nombre_en varchar(200) NOT NULL,
            iso2 varchar(2) NULL,
            iso3 varchar(3) NULL,
            codigo varchar(4) NULL,
            activo int2 DEFAULT 1 NULL,
            CONSTRAINT ge_pais_nombre_en_uk UNIQUE (nombre_en),
            CONSTRAINT ge_pais_nombre_es_uk UNIQUE (nombre_es),
            CONSTRAINT ge_pais_pk PRIMARY KEY (pais_id)
        );
        """)
    op.execute(
        """
        INSERT INTO ge_pais VALUES (1, 'Afganistán', 'Afghanistan', 'AF', 'AFG', '004', 1);
        INSERT INTO ge_pais VALUES (2, 'Albania', 'Albania', 'AL', 'ALB', '008', 1);
        INSERT INTO ge_pais VALUES (3, 'Argelia', 'Algeria', 'DZ', 'DZA', '012', 1);
        INSERT INTO ge_pais VALUES (4, 'Samoa Americana', 'American Samoa', 'AS', 'ASM', '016', 1);
        INSERT INTO ge_pais VALUES (5, 'Andorra', 'Andorra', 'AD', 'AND', '020', 1);
        INSERT INTO ge_pais VALUES (6, 'Angola', 'Angola', 'AO', 'AGO', '024', 1);
        INSERT INTO ge_pais VALUES (7, 'Anguila', 'Anguilla', 'AI', 'AIA', '660', 1);
        INSERT INTO ge_pais VALUES (8, 'Antártida', 'Antarctica', 'AQ', 'ATA', '010', 1);
        INSERT INTO ge_pais VALUES (9, 'Antigua y Barbuda', 'Antigua and Barbuda', 'AG', 'ATG', '028', 1);
        INSERT INTO ge_pais VALUES (10, 'Argentina', 'Argentina', 'AR', 'ARG', '032', 1);
        INSERT INTO ge_pais VALUES (11, 'Armenia', 'Armenia', 'AM', 'ARM', '051', 1);
        INSERT INTO ge_pais VALUES (12, 'Aruba', 'Aruba', 'AW', 'ABW', '533', 1);
        INSERT INTO ge_pais VALUES (13, 'Australia', 'Australia', 'AU', 'AUS', '036', 1);
        INSERT INTO ge_pais VALUES (14, 'Austria', 'Austria', 'AT', 'AUT', '040', 1);
        INSERT INTO ge_pais VALUES (15, 'Azerbaiyán 1', 'Azerbaijan', 'AZ', 'AZE', '031', 1);
        INSERT INTO ge_pais VALUES (16, 'Bahamas', 'Bahamas', 'BS', 'BHS', '044', 1);
        INSERT INTO ge_pais VALUES (17, 'Baréin', 'Bahrain', 'BH', 'BHR', '048', 1);
        INSERT INTO ge_pais VALUES (18, 'Bangladesh', 'Bangladesh', 'BD', 'BGD', '050', 1);
        INSERT INTO ge_pais VALUES (19, 'Barbados', 'Barbados', 'BB', 'BRB', '052', 1);
        INSERT INTO ge_pais VALUES (20, 'Bielorrusia', 'Belarus', 'BY', 'BLR', '112', 1);
        INSERT INTO ge_pais VALUES (21, 'Bélgica', 'Belgium', 'BE', 'BEL', '056', 1);
        INSERT INTO ge_pais VALUES (22, 'Belice', 'Belize', 'BZ', 'BLZ', '084', 1);
        INSERT INTO ge_pais VALUES (23, 'Benín', 'Benin', 'BJ', 'BEN', '204', 1);
        INSERT INTO ge_pais VALUES (24, 'Bermudas', 'Bermuda', 'BM', 'BMU', '060', 1);
        INSERT INTO ge_pais VALUES (25, 'Bután', 'Bhutan', 'BT', 'BTN', '064', 1);
        INSERT INTO ge_pais VALUES (26, 'Bolivia', 'Bolivia', 'BO', 'BOL', '068', 1);
        INSERT INTO ge_pais VALUES (27, 'Bosnia y Herzegovina', 'Bosnia and Herzegovina', 'BA', 'BIH', '070', 1);
        INSERT INTO ge_pais VALUES (28, 'Botsuana', 'Botswana', 'BW', 'BWA', '072', 1);
        INSERT INTO ge_pais VALUES (29, 'Isla Bouvet', 'Bouvet Island', 'BV', 'BVT', '074', 1);
        INSERT INTO ge_pais VALUES (30, 'Brasil', 'Brazil', 'BR', 'BRA', '076', 1);
        INSERT INTO ge_pais VALUES (31, 'Territorio Británico del Océano Índico', 'British Indian Ocean Territory', 'IO', 'IOT', '086', 1);
        INSERT INTO ge_pais VALUES (32, 'Brunei', 'Brunei Darussalam', 'BN', 'BRN', '096', 1);
        INSERT INTO ge_pais VALUES (33, 'Bulgaria', 'Bulgaria', 'BG', 'BGR', '100', 1);
        INSERT INTO ge_pais VALUES (34, 'Burkina Faso', 'Burkina Faso', 'BF', 'BFA', '854', 1);
        INSERT INTO ge_pais VALUES (35, 'Burundi', 'Burundi', 'BI', 'BDI', '108', 1);
        INSERT INTO ge_pais VALUES (36, 'Cabo Verde', 'Cabo Verde', 'CV', 'CPV', '132', 1);
        INSERT INTO ge_pais VALUES (37, 'Camboya', 'Cambodia', 'KH', 'KHM', '116', 1);
        INSERT INTO ge_pais VALUES (38, 'Camerún', 'Cameroon', 'CM', 'CMR', '120', 1);
        INSERT INTO ge_pais VALUES (39, 'Canadá', 'Canada', 'CA', 'CA', '124', 1);
        INSERT INTO ge_pais VALUES (40, 'Islas Caimán', 'Cayman Islands', 'KY', 'CYM', '136', 1);
        INSERT INTO ge_pais VALUES (41, 'República Centroafricana', 'Central African Republic', 'CF', 'CYM', '140', 1);
        INSERT INTO ge_pais VALUES (42, 'Chad', 'Chad', 'TD', 'TCD', '148', 1);
        INSERT INTO ge_pais VALUES (43, 'Chile', 'Chile', 'CL', 'CHL', '152', 1);
        INSERT INTO ge_pais VALUES (44, 'China', 'China', 'CN', 'CHN', '156', 1);
        INSERT INTO ge_pais VALUES (45, 'Isla de Navidad', 'Christmas Island', 'CX', 'CXR', '162', 1);
        INSERT INTO ge_pais VALUES (46, 'Islas Cocos (Keeling)', 'Cocos (Keeling) Islands', 'CC', 'CCK', '166', 1);
        INSERT INTO ge_pais VALUES (47, 'Colombia', 'Colombia', 'CO', 'COL', '170', 1);
        INSERT INTO ge_pais VALUES (48, 'Comoras', 'Comoros', 'KM', 'COM', '174', 1);
        INSERT INTO ge_pais VALUES (49, 'República Democrática del Congo', 'Democratic Republic of the Congo', 'CD', 'COD', '180', 1);
        INSERT INTO ge_pais VALUES (50, 'Congo', 'Congo', 'CG', 'COG', '178', 1);
        INSERT INTO ge_pais VALUES (51, 'Islas Cook', 'Cook Islands', 'CK', 'COK', '184', 1);
        INSERT INTO ge_pais VALUES (52, 'Costa Rica', 'Costa Rica', 'CR', 'CRI', '188', 1);
        INSERT INTO ge_pais VALUES (53, 'Croacia', 'Croatia', 'HR', 'HRV', '191', 1);
        INSERT INTO ge_pais VALUES (54, 'Cuba', 'Cuba', 'CU', 'CUB', '192', 1);
        INSERT INTO ge_pais VALUES (55, 'Curazao', 'Curaçao', 'CW', 'CUW', '531', 1);
        INSERT INTO ge_pais VALUES (56, 'Chipre', 'Cyprus', 'CY', 'CYP', '196', 1);
        INSERT INTO ge_pais VALUES (57, 'Chequia', 'Czechia', 'CZ', 'CZE', '203', 1);
        INSERT INTO ge_pais VALUES (58, 'Costa de Marfil', 'Côte d''Ivoire', 'CI', 'CIV', '384', 1);
        INSERT INTO ge_pais VALUES (59, 'Dinamarca', 'Denmark', 'DK', 'DNK', '208', 1);
        INSERT INTO ge_pais VALUES (60, 'Yibuti', 'Djibouti', 'DJ', 'DJI', '262', 1);
        INSERT INTO ge_pais VALUES (61, 'Dominica', 'Dominica', 'DM', 'DMA', '212', 1);
        INSERT INTO ge_pais VALUES (62, 'República Dominicana', 'Dominican Republic', 'DO', 'DOM', '214', 1);
        INSERT INTO ge_pais VALUES (63, 'Ecuador', 'Ecuador', 'EC', 'ECU', '218', 1);
        INSERT INTO ge_pais VALUES (64, 'Egipto', 'Egypt', 'EG', 'EGY', '818', 1);
        INSERT INTO ge_pais VALUES (65, 'El Salvador', 'El Salvador', 'SV', 'SLV', '222', 1);
        INSERT INTO ge_pais VALUES (66, 'Guinea Ecuatorial', 'Equatorial Guinea', 'GQ', 'GNQ', '226', 1);
        INSERT INTO ge_pais VALUES (67, 'Eritrea', 'Eritrea', 'ER', 'ERI', '232', 1);
        INSERT INTO ge_pais VALUES (68, 'Estonia', 'Estonia', 'EE', 'EST', '233', 1);
        INSERT INTO ge_pais VALUES (69, 'Esuatini', 'Eswatini', 'SZ', 'SWZ', '748', 1);
        INSERT INTO ge_pais VALUES (70, 'Etiopía', 'Ethiopia', 'ET', 'ETH', '231', 1);
        INSERT INTO ge_pais VALUES (71, 'Islas Malvinas', 'Falkland Islands', 'FK', 'FLK', '238', 1);
        INSERT INTO ge_pais VALUES (72, 'Islas Feroe', 'Faroe Islands', 'FO', 'FRO', '234', 1);
        INSERT INTO ge_pais VALUES (73, 'Fiyi', 'Fiji', 'FJ', 'FJI', '242', 1);
        INSERT INTO ge_pais VALUES (74, 'Finlandia', 'Finland', 'FI', 'FIN', '246', 1);
        INSERT INTO ge_pais VALUES (75, 'Francia', 'France', 'FR', 'FRA', '250', 1);
        INSERT INTO ge_pais VALUES (76, 'Guayana Francesa', 'French Guiana', 'GF', 'GUF', '254', 1);
        INSERT INTO ge_pais VALUES (77, 'Polinesia Francesa', 'French Polynesia', 'PF', 'PYF', '258', 1);
        INSERT INTO ge_pais VALUES (78, 'Territorios Australes Franceses', 'French Southern Territories', 'TF', 'ATF', '260', 1);
        INSERT INTO ge_pais VALUES (79, 'Gabón', 'Gabon', 'GA', 'GAB', '266', 1);
        INSERT INTO ge_pais VALUES (80, 'Gambia', 'Gambia', 'GM', 'GMB', '270', 1);
        INSERT INTO ge_pais VALUES (81, 'Georgia', 'Georgia', 'GE', 'GEO', '268', 1);
        INSERT INTO ge_pais VALUES (82, 'Alemania', 'Germany', 'DE', 'DEU', '276', 1);
        INSERT INTO ge_pais VALUES (83, 'Ghana', 'Ghana', 'GH', 'GHA', '288', 1);
        INSERT INTO ge_pais VALUES (84, 'Gibraltar', 'Gibraltar', 'GI', 'GIB', '292', 1);
        INSERT INTO ge_pais VALUES (85, 'Grecia', 'Greece', 'GR', 'GRC', '300', 1);
        INSERT INTO ge_pais VALUES (86, 'Groenlandia', 'Greenland', 'GL', 'GRL', '304', 1);
        INSERT INTO ge_pais VALUES (87, 'Granada', 'Grenada', 'GD', 'GRD', '308', 1);
        INSERT INTO ge_pais VALUES (88, 'Guadalupe', 'Guadeloupe', 'GP', 'GLP', '312', 1);
        INSERT INTO ge_pais VALUES (89, 'Guam', 'Guam', 'GU', 'GUM', '316', 1);
        INSERT INTO ge_pais VALUES (90, 'Guatemala', 'Guatemala', 'GT', 'GTM', '320', 1);
        INSERT INTO ge_pais VALUES (91, 'Guernsey', 'Guernsey', 'GG', 'GGY', '831', 1);
        INSERT INTO ge_pais VALUES (92, 'Guinea', 'Guinea', 'GN', 'GIN', '324', 1);
        INSERT INTO ge_pais VALUES (93, 'Guinea-Bissau', 'Guinea-Bissau', 'GW', 'GNB', '624', 1);
        INSERT INTO ge_pais VALUES (94, 'Guyana', 'Guyana', 'GY', 'GUY', '328', 1);
        INSERT INTO ge_pais VALUES (95, 'Haití', 'Haiti', 'HT', 'HTI', '332', 1);
        INSERT INTO ge_pais VALUES (96, 'Isla Heard e Islas McDonald', 'Heard Island and McDonald Islands', 'HM', 'HMD', '334', 1);
        INSERT INTO ge_pais VALUES (97, 'Santa Sede (Ciudad del Vaticano)', 'Holy See (Vatican City State)', 'VA', 'VAT', '336', 1);
        INSERT INTO ge_pais VALUES (98, 'Honduras', 'Honduras', 'HN', 'HND', '340', 1);
        INSERT INTO ge_pais VALUES (99, 'Hong Kong', 'Hong Kong', 'HK', 'HKG', '344', 1);
        INSERT INTO ge_pais VALUES (100, 'Hungría', 'Hungary', 'HU', 'HUN', '348', 1);
        INSERT INTO ge_pais VALUES (101, 'Islandia', 'Iceland', 'IS', 'ISL', '352', 1);
        INSERT INTO ge_pais VALUES (102, 'India', 'India', 'IN', 'IND', '356', 1);
        INSERT INTO ge_pais VALUES (103, 'Indonesia', 'Indonesia', 'ID', 'IDN', '360', 1);
        INSERT INTO ge_pais VALUES (104, 'República Islámica de Irán', 'Islamic Republic of Iran', 'IR', 'IRN', '364', 1);
        INSERT INTO ge_pais VALUES (105, 'Irak', 'Iraq', 'IQ', 'IRQ', '368', 1);
        INSERT INTO ge_pais VALUES (106, 'Irlanda', 'Ireland', 'IE', 'IRL', '372', 1);
        INSERT INTO ge_pais VALUES (107, 'Isla de Man', 'Isle of Man', 'IM', 'IMN', '833', 1);
        INSERT INTO ge_pais VALUES (108, 'Israel', 'Israel', 'IL', 'ISR', '376', 1);
        INSERT INTO ge_pais VALUES (109, 'Italia', 'Italy', 'IT', 'ITA', '380', 1);
        INSERT INTO ge_pais VALUES (110, 'Jamaica', 'Jamaica', 'JM', 'JAM', '388', 1);
        INSERT INTO ge_pais VALUES (111, 'Japón', 'Japan', 'JP', 'JPN', '392', 1);
        INSERT INTO ge_pais VALUES (112, 'Jersey', 'Jersey', 'JE', 'JEY', '832', 1);
        INSERT INTO ge_pais VALUES (113, 'Jordania', 'Jordan', 'JO', 'JOR', '400', 1);
        INSERT INTO ge_pais VALUES (114, 'Kazajistán', 'Kazakhstan', 'KZ', 'KAZ', '398', 1);
        INSERT INTO ge_pais VALUES (115, 'Kenia', 'Kenya', 'KE', 'KEN', '404', 1);
        INSERT INTO ge_pais VALUES (116, 'Kiribati', 'Kiribati', 'KI', 'KIR', '296', 1);
        INSERT INTO ge_pais VALUES (117, 'Corea del Norte', 'Democratic People''s Republic of Korea', 'KP', 'PRK', '408', 1);
        INSERT INTO ge_pais VALUES (118, 'Corea del Sur', 'Republic of Korea', 'KR', 'KOR', '410', 1);
        INSERT INTO ge_pais VALUES (119, 'Kuwait', 'Kuwait', 'KW', 'KWT', '414', 1);
        INSERT INTO ge_pais VALUES (120, 'Kirguistán', 'Kyrgyzstan', 'KG', 'KGZ', '417', 1);
        INSERT INTO ge_pais VALUES (121, 'Laos', 'Lao People''s Democratic Republic', 'LA', 'LAO', '418', 1);
        INSERT INTO ge_pais VALUES (122, 'Letonia', 'Latvia', 'LV', 'LVA', '428', 1);
        INSERT INTO ge_pais VALUES (123, 'Líbano', 'Lebanon', 'LB', 'LBN', '422', 1);
        INSERT INTO ge_pais VALUES (124, 'Lesoto', 'Lesotho', 'LS', 'LSO', '426', 1);
        INSERT INTO ge_pais VALUES (125, 'Liberia', 'Liberia', 'LR', 'LBR', '430', 1);
        INSERT INTO ge_pais VALUES (126, 'Libia', 'Libya', 'LY', 'LBY', '434', 1);
        INSERT INTO ge_pais VALUES (127, 'Liechtenstein', 'Liechtenstein', 'LI', 'LIE', '438', 1);
        INSERT INTO ge_pais VALUES (128, 'Lituania', 'Lithuania', 'LT', 'LTU', '440', 1);
        INSERT INTO ge_pais VALUES (129, 'Luxemburgo', 'Luxembourg', 'LU', 'LUX', '442', 1);
        INSERT INTO ge_pais VALUES (130, 'Macao', 'Macao', 'MO', 'MAC', '446', 1);
        INSERT INTO ge_pais VALUES (131, 'Madagascar', 'Madagascar', 'MG', 'MDG', '450', 1);
        INSERT INTO ge_pais VALUES (132, 'Malaui', 'Malawi', 'MW', 'MWI', '454', 1);
        INSERT INTO ge_pais VALUES (133, 'Malasia', 'Malaysia', 'MY', 'MYS', '458', 1);
        INSERT INTO ge_pais VALUES (134, 'Maldivas', 'Maldives', 'MV', 'MDV', '462', 1);
        INSERT INTO ge_pais VALUES (135, 'Malí', 'Mali', 'ML', 'MLI', '466', 1);
        INSERT INTO ge_pais VALUES (136, 'Malta', 'Malta', 'MT', 'MLT', '470', 1);
        INSERT INTO ge_pais VALUES (137, 'Islas Marshall', 'Marshall Islands', 'MH', 'MHL', '584', 1);
        INSERT INTO ge_pais VALUES (138, 'Martinica', 'Martinique', 'MQ', 'MTQ', '474', 1);
        INSERT INTO ge_pais VALUES (139, 'Mauritania', 'Mauritania', 'MR', 'MRT', '478', 1);
        INSERT INTO ge_pais VALUES (140, 'Mauricio', 'Mauritius', 'MU', 'MUS', '480', 1);
        INSERT INTO ge_pais VALUES (141, 'Mayotte', 'Mayotte', 'YT', 'MYT', '175', 1);
        INSERT INTO ge_pais VALUES (142, 'México', 'Mexico', 'MX', 'MEX', '484', 1);
        INSERT INTO ge_pais VALUES (143, 'Micronesia (Estados Federados de)', 'Micronesia (Federated States of)', 'FM', 'FSM', '583', 1);
        INSERT INTO ge_pais VALUES (144, 'Moldavia', 'Moldova', 'MD', 'MDA', '498', 1);
        INSERT INTO ge_pais VALUES (145, 'Mónaco', 'Monaco', 'MC', 'MCO', '492', 1);
        INSERT INTO ge_pais VALUES (146, 'Mongolia', 'Mongolia', 'MN', 'MNG', '496', 1);
        INSERT INTO ge_pais VALUES (147, 'Montenegro', 'Montenegro', 'ME', 'MNE', '499', 1);
        INSERT INTO ge_pais VALUES (148, 'Montserrat', 'Montserrat', 'MS', 'MSR', '500', 1);
        INSERT INTO ge_pais VALUES (149, 'Marruecos', 'Morocco', 'MA', 'MAR', '504', 1);
        INSERT INTO ge_pais VALUES (150, 'Mozambique', 'Mozambique', 'MZ', 'MOZ', '508', 1);
        INSERT INTO ge_pais VALUES (151, 'Myanmar (Birmania)', 'Myanmar (Burma)', 'MM', 'MMR', '104', 1);
        INSERT INTO ge_pais VALUES (152, 'Namibia', 'Namibia', 'NA', 'NAM', '516', 1);
        INSERT INTO ge_pais VALUES (153, 'Nauru', 'Nauru', 'NR', 'NRU', '520', 1);
        INSERT INTO ge_pais VALUES (154, 'Nepal', 'Nepal', 'NP', 'NPL', '524', 1);
        INSERT INTO ge_pais VALUES (155, 'Países Bajos', 'Netherlands', 'NL', 'NLD', '528', 1);
        INSERT INTO ge_pais VALUES (156, 'Nueva Caledonia', 'New Caledonia', 'NC', 'NCL', '540', 1);
        INSERT INTO ge_pais VALUES (157, 'Nueva Zelanda', 'New Zealand', 'NZ', 'NZL', '554', 1);
        INSERT INTO ge_pais VALUES (158, 'Nicaragua', 'Nicaragua', 'NI', 'NIC', '558', 1);
        INSERT INTO ge_pais VALUES (159, 'Níger', 'Niger', 'NE', 'NER', '562', 1);
        INSERT INTO ge_pais VALUES (160, 'Nigeria', 'Nigeria', 'NG', 'NGA', '566', 1);
        INSERT INTO ge_pais VALUES (161, 'Niue', 'Niue', 'NU', 'NIU', '570', 1);
        INSERT INTO ge_pais VALUES (162, 'Isla Norfolk', 'Norfolk Island', 'NF', 'NFK', '574', 1);
        INSERT INTO ge_pais VALUES (163, 'Islas Marianas del Norte', 'Northern Mariana Islands', 'MP', 'MNP', '580', 1);
        INSERT INTO ge_pais VALUES (164, 'Noruega', 'Norway', 'NO', 'NOR', '578', 1);
        INSERT INTO ge_pais VALUES (165, 'Omán', 'Oman', 'OM', 'OMN', '512', 1);
        INSERT INTO ge_pais VALUES (166, 'Pakistán', 'Pakistan', 'PK', 'PAK', '586', 1);
        INSERT INTO ge_pais VALUES (167, 'Palau', 'Palau', 'PW', 'PLW', '585', 1);
        INSERT INTO ge_pais VALUES (168, 'Palestina', 'Palestine', 'PS', 'PSE', '275', 1);
        INSERT INTO ge_pais VALUES (169, 'Panamá', 'Panama', 'PA', 'PAN', '591', 1);
        INSERT INTO ge_pais VALUES (170, 'Papúa Nueva Guinea', 'Papua New Guinea', 'PG', 'PNG', '598', 1);
        INSERT INTO ge_pais VALUES (171, 'Paraguay', 'Paraguay', 'PY', 'PRY', '600', 1);
        INSERT INTO ge_pais VALUES (172, 'Peru', 'Peru', 'PE', 'PER', '604', 1);
        INSERT INTO ge_pais VALUES (173, 'Filipinas', 'Philippines', 'PH', 'PHL', '608', 1);
        INSERT INTO ge_pais VALUES (174, 'Islas Pitcairn', 'Pitcairn Islands', 'PN', 'PCN', '612', 1);
        INSERT INTO ge_pais VALUES (175, 'Polonia', 'Poland', 'PL', 'POL', '616', 1);
        INSERT INTO ge_pais VALUES (176, 'Portugal', 'Portugal', 'PT', 'PRT', NULL, 1);
        """)


def downgrade_engine1() -> None:
    """Downgrade engine1 schema."""
    op.drop_table('ge_pais')

