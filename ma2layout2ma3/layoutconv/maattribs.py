"""MA attributumok osztályai."""


class ma2attribs(object):
    """MA2 osztályok."""

    def __init__(self):
        """Osztály inicializáció."""
        self.info = {
            "datetime": "2022-10-02T13:45:31",
            "showfile": "hutlen_feleseg_tarr",
        }
        self.group = {
            "index": "0",
            "name": "Robotok",
        }
        self.subfixtures = {"fix_id": "41", "sub_index": "1", "cha_id": "255"}
        self.layoutdata = {
            "index": "0",
            "marker_visible": "true",
            "snap_always_active": "true",
            "background_color": "000000",
            "visible_grid_h": "0",
            "visible_grid_w": "0",
            "snap_grid_h": "0.5",
            "snap_grid_w": "0.5",
            "default_gauge": "Filled& Symbol",
            "subfixture_view_mode": "DMX Layer",
        }
        self.layoutsubfix = {
            "font_size": "Small",
            "center_x": "-12.338",
            "center_y": "-0.175",
            "size_h": "2",
            "size_w": "2",
            "background_color": "00000000",
            "border_color": "f400ff",
            "text_color": "ff00ff",
            "icon": "None",
            "gauge_style": "Spot",
            "show_id": "1",
            "show_name": "1",
            "show_type": "1",
            "show_dimmer_bar": "Off",
            "function_type": "Filled",
            "select_group": "1",
            "image_size": "Fit",
        }
        self.image = {"name": "Moving 2 8", "no": 8}

    def __str__(self):
        """Info, csoport,alcsoport visszaadása."""
        return f"Info:{self.info} \nGroup:{self.group}\nSubfixture:{self.subfixtures}"


class ma3attribs(object):
    """MA3 osztályok."""

    def __init__(self):
        """Inicializálás."""
        self.layout = {
            "Name": "Tarantula",
            "Guid": "EF AB FA 0D 58 7F DE 0B 78 DD 40 1D BC 69 8A FE",
            "PositionX": "0",
            "PositionY": "0",
            "DimensionW": "1920",
            "DimensionH": "1080",
            "ViewPosActive": "No",
            "ViewPosScale": "0.0000000000",
            "ViewPosX": "-7000",
            "ViewPosY": "-7000",
            "AxisSystem": "Stage",
            "RotationMode": "Group",
            "LayoutType": "Line",
            "AxisGroupType": "XY",
            "EncoderFunction": "Position",
            "GridDirection": "First X then Y",
            "GridRowOrder": "Up Down",
            "GridColumnOrder": "Left Right",
            "Columns": "10",
            "Rows": "5",
            "ColumnsInterval": "50.000",
            "RowsInterval": "50.000",
            "StartX": "0.000",
            "LengthX": "1000.000",
            "StartY": "0.000",
            "LengthY": "0.000",
            "StartZ": "0.000",
            "LengthZ": "0.000",
            "RadiusStart": "300.000",
            "RadiusDelta": "0.000",
            "AngleStart": "0.000",
            "AngleRange": "360.000",
            "CameraIndex": "1 'Auto'",
            "Scale": "1.00",
            "Ratio": "1.00",
            "MoveX": "0",
            "MoveY": "0",
            "ArrangeOnChange": "No",
            "SendChangesWhileEncoderEvent": "No",
        }

        self.element = {
            "Name": "RTara2 1",
            "Guid": "EF AB FA 0D CF 61 81 2A 2C 19 D2 93 B2 19 0F F8",
            "Object": "ShowData.LivePatch.Stages.Stage 1.Fixtures.Robe Tarantula.RTara2 1",
            "Action": "SelFix",
            "PosX": "-960",
            "PosY": "340",
            "PositionW": "200",
            "PositionH": "200",
            "BorderSize": "1",
            "VisibilityElement": "Visible",
            "VisibilityBar": "Hidden",
            "VisibilityObjectName": "Visible",
            "VisibilityID": "Hidden",
            "VisibilityCID": "Hidden",
            "VisibilityBorder": "Visible",
            "VisibilityValue": "Visible",
            "VisibilityIndicatorBar": "Hidden",
            "VisibilitySelectionRelevance": "No",
            "TextColor": "FFFFFFFF",
            "TextAlignmentH": "Center",
            "TextAlignmentV": "Center",
            "FontSize": "Default",
            "BorderColor": "808080FF",
        }
