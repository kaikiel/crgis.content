# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from crgis.content import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.textfield import RichText as RichTextField
from plone.supermodel           import model
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from zope.schema.vocabulary     import SimpleVocabulary
from zope.schema.vocabulary     import SimpleTerm
from plone.autoform             import directives
from plone.app.vocabularies.catalog import CatalogSource
from z3c.form.browser.radio     import RadioFieldWidget
from z3c.form.browser.checkbox  import CheckBoxFieldWidget
from plone.dexterity.content    import Container


class FolderishContent(Container):
    pass

class ICrgisContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class ITemple(model.Schema):
    """Temple Type"""
    id = schema.TextLine(
        title=_(u"Code"),
	required=True,
	description =_(u"A String Based on Abbreviation of Administrative Area.")
    )
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    directives.widget(data_src=RadioFieldWidget)
    data_src = schema.Choice(
        title=_(u"Data Source"),
        vocabulary='vocabulary.data_src',
        required=False,
    )

    directives.widget(coordinate=RadioFieldWidget)
    coordinate = schema.Choice(
        title=_(u"Coordinate Type"),
        vocabulary='vocabulary.coordinate',
        required=False,
    )

    facing = schema.TextLine(
        title=_(u"Sitting Facing"),
        required=False,
    )
    
    deity_host = schema.Tuple(
        title=_(u"Deity Host"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.deity_name',
        ),
        missing_value=()
    )
    deity_host_o = schema.TextLine(
        title=_(u"Deity Host Other"),
        required=False,
    )
    deity_host_a = schema.TextLine(
        title=_(u"Deity Host Alias"),
        required=False,
    )
    deity_company = schema.Tuple(
        title=_(u"Deity Company"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.deity_name',
        ),
        missing_value=()
    )
    
    directives.widget(religion=RadioFieldWidget)
    religion = schema.Choice(
        title=_(u"Religion Type"),
        vocabulary='vocabulary.religion',
        required=False,
    )
    religion_o = schema.TextLine(
        title=_(u"Religion Type Other"),
        required=False,
    )

    directives.widget(building=RadioFieldWidget)
    building = schema.Choice(
        title=_(u"Building Type"),
        vocabulary='vocabulary.building',
        required=False,
    )
    building_o = schema.TextLine(
        title=_(u"Building Type Other"),
        required=False,
    )
    registered = schema.TextLine(
        title=_(u"Registered Name"),
        required=False,
    )

    directives.widget(funding=RadioFieldWidget)
    funding = schema.Choice(
        title=_(u"Funding Type"),
        vocabulary='vocabulary.funding',
        required=False,
    )

    directives.widget(organizing=RadioFieldWidget)
    organizing = schema.Choice(
        title=_(u"Organizing Type"),
        vocabulary='vocabulary.organizing',
        required=False,
    )
    organizing_o = schema.TextLine(
        title=_(u"Organizing Type Other"),
        required=False,
    )
    address = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )
    in_charge = schema.TextLine(
        title=_(u"Person In Charge"),
        required=False,
    )
    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
    )
    homepage = schema.TextLine(
        title=_(u"Homepage"),
        required=False,
    )
    era = schema.TextLine(
        title=_(u"Estimated Earliest Founding Year"),
        required=False,
    )
    era_end = schema.TextLine(
        title=_(u"Estimated Latest Founding Year"),
        required=False,
    )

    directives.widget(year_accuracy=RadioFieldWidget)
    year_accuracy = schema.Choice(
        title=_(u"Year Accuracy"),
        vocabulary='vocabulary.year_accuracy',
        required=False,
    )
    history = RichTextField(
        title=_(u"Establishment History"),
        required=False,
    )
    era_1 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Collection"),
        required=False,
    )
    era_2 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Overview"),
        required=False,
    )
    era_ref = RichTextField(
        title=_(u"References on Establishment"),
        required=False,
    )
    deity_accompany = RichTextField(
        title=_(u"Deities Accompany"),
        required=False,
    )
    worship = RichTextField(
        title=_(u"Worship"),
        required=False,
    )
    introduction = RichTextField(
        title=_(u"Introduction"),
        required=False,
    )
    overview = RichTextField(
        title=_(u"Building Overview"),
        required=False,
    )
    antiquity = RichTextField(
        title=_(u"Antiquity"),
        required=False,
    )
    narrate = RichTextField(
        title=_(u"Narrate"),
        required=False,
    )
    non_narrate = RichTextField(
        title=_(u"Non Narrate"),
        required=False,
    )
    academic = RichTextField(
        title=_(u"Academic Works"),
        required=False,
    )
    literature = RichTextField(
        title=_(u"Literature Reference"),
        required=False,
    )
    fill_in = schema.TextLine(
        title=_(u"Filling Person"),
        required=False,
    )
    fill_date = schema.Datetime(
        title=_(u"Filling Date"),
        required=False,
    )
    model.fieldset('appendix', label=_(u'Appendix'), fields=['jstq', 'jstq_o', 'jsfw', 'xyfw', 'flxt', 'flxt_o', 'ymmy', 'ymmy_o', 'xhly', 'xhly_o', 'nlqs', 'nlqs_o', 'wyxx', 'wyxx_o', 'medicine', 'luck', 'organization', 'desc_o'])
    
    directives.widget(jstq=CheckBoxFieldWidget)
    jstq = schema.List(
        title=_(u"JiSiZuQun"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.jstq',
        ),
        missing_value=()
    )
    jstq_o = schema.TextLine(
        title=_(u"JiSiZuQun Other"),
        required=False,
    )
    jsfw = RichTextField(
        title=_(u"JiSiFanWei"),
        required=False,
    )
    xyfw = RichTextField(
        title=_(u"XinYangFangWei"),
        required=False,
    )

    directives.widget(flxt=CheckBoxFieldWidget)
    flxt = schema.Tuple(
        title=_(u"FenLingXiTong"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.flxt',
        ),
        missing_value=()
    )
    flxt_o = schema.TextLine(
        title=_(u"FenLingXiTong Other"),
        required=False,
    )

    directives.widget(ymmy=CheckBoxFieldWidget)
    ymmy = schema.Tuple(
        title=_(u"YiMingMiaoYu"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.ymmy',
        ),
        missing_value=()
    )
    ymmy_o = schema.TextLine(
        title=_(u"YiMingMiaoYu Other"),
        required=False,
    )

    directives.widget(xhly=CheckBoxFieldWidget)
    xhly = schema.Tuple(
        title=_(u"XiangHuoLaiYuan"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.xhly',
        ),
        missing_value=()
    )
    xhly_o = schema.TextLine(
        title=_(u"XiangHuoLaiYuan Other"),
        required=False,
    )

    directives.widget(nlqs=CheckBoxFieldWidget)
    nlqs = schema.Tuple(
        title=_(u"NianLiQingSheng"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.nlqs',
        ),
        missing_value=()
    )
    nlqs_o = schema.TextLine(
        title=_(u"NianLiQingSheng Other"),
        required=False,
    )
    
    directives.widget(wyxx=CheckBoxFieldWidget)
    wyxx = schema.Tuple(
        title=_(u"WangYeXianXiang"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.wyxx',
        ),
        missing_value=()
    )
    wyxx_o = schema.TextLine(
        title=_(u"WangYeXianXiang Other"),
        required=False,
    )

    directives.widget(medicine=CheckBoxFieldWidget)
    medicine = schema.Tuple(
        title=_(u"Medicine Divination"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.medicine',
        ),
        missing_value=()
    )

    directives.widget(luck=CheckBoxFieldWidget)
    luck = schema.Tuple(
        title=_(u"Luck Divination"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.luck',
        ),
        missing_value=()
    )
    organization = RichTextField(
        title=_(u"Believer Organization"),
        required=False,
    )
    desc_o = RichTextField(
        title=_(u"Description Other"),
        required=False,
    )
    model.fieldset('wangye', label=_(u'WangYe'), fields=['wysm', 'yswt', 'dtxs', 'freq', 'wttz', 'swxs', 'ysgs'])
    wysm = schema.TextLine(
        title=_(u"WangYe Name"),
        required=False,
    )
    yswt = schema.TextLine(
        title=_(u"YungS WangTsuan"),
        required=False,
    )
    dtxs = schema.Tuple(
        title=_(u"DaiTien XuanSho"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    freq = schema.Tuple(
        title=_(u"Frequence"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    wttz = schema.Tuple(
        title=_(u"WangTsuan Material"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=()
    )
    swxs = schema.TextLine(
        title=_(u"SungWang XingShi"),
        required=False,
    )
    ysgs = RichTextField(
        title=_(u"YSGS"),
        required=False,
    )

class IBiXieWu(model.Schema):
    """BiXieWu Type"""
    id = schema.TextLine(
        title=_(u"Code"),
	required=True,
	description =_(u"A String Based on Abbreviation of Administrative Area.")
    )
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )
    
    directives.widget(data_src=RadioFieldWidget) 
    data_src = schema.Choice(
        title=_(u"Data Source"),
        vocabulary='vocabulary.data_src',
        required=False,
    )
    lct_cou = schema.TextLine(
        title=_(u"County"),
        required=False,
    )
    lct_tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
    )
    lct_vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
    )
 
    directives.widget(coordinate=RadioFieldWidget) 
    coordinate = schema.Choice(
        title=_(u"Coordinate Type"),
        vocabulary='vocabulary.coordinate',
        required=False,
    )
 
    directives.widget(btype=RadioFieldWidget) 
    btype = schema.Choice(
        title=_(u"BiXieWu_Type"),
        vocabulary='vocabulary.bixiewu',
        required=False,
    )
    era = schema.TextLine(
        title=_(u"Common Era"),
        required=False,
    )
    era_ref = RichTextField(
        title=_(u"Era Reference"),
        required=False,
    )
    facing = schema.TextLine(
        title=_(u"Facing"),
        required=False,
    )

    directives.widget(material=RadioFieldWidget) 
    material = schema.Choice(
        title=_(u"Material"),
        vocabulary='vocabulary.material',
        required=False,
    )
    volume = RichTextField(
        title=_(u"Volume"),
        required=False,
    )

    directives.widget(locational=RadioFieldWidget) 
    locational = schema.Choice(
        title=_(u"Locational Attribute"),
        vocabulary='vocabulary.locational',
        required=False,
    )
    purpose = schema.Tuple(
        title=_(u"Purpose"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.purpose',
        ),
        missing_value=()
    )
    worship = RichTextField(
        title=_(u"Worship Description"),
        required=False,
    )
    establishment = RichTextField(
        title=_(u"Establishment Description"),
        required=False,
    )
    spatial = RichTextField(
        title=_(u"Spatial Attribute"),
        required=False,
    )
    environment = RichTextField(
        title=_(u"Environment Description"),
        required=False,
    )
    reference = RichTextField(
        title=_(u"Reference"),
        required=False,
    )
    remark = RichTextField(
        title=_(u"Remark"),
        required=False,
    )
    r_temples = RelationList(
        title=_(u"Related Temples"),
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            source=CatalogSource(portal_type='Temple')
        ),
        required=False,
    )
    model.fieldset('fengshiye', label=_(u'FengShiYe'), fields=['village', 'color', 'genre', 'posture', 'gender', 'shi_d', 'shi_w', 'shi_h', 'shi_t', 'base_l', 'base_w', 'base_h'])
    village = schema.TextLine(
        title=_(u"Village Name"),
        required=False,
    )

    directives.widget(color=RadioFieldWidget)
    color = schema.Choice(
        title=_(u"Color"),
        vocabulary='vocabulary.isExisting',
        required=False,
    )

    directives.widget(genre=RadioFieldWidget)
    genre = schema.Choice(
        title=_(u"Genre"),
        vocabulary='vocabulary.genre',
        required=False,
    )

    directives.widget(posture=RadioFieldWidget)
    posture = schema.Choice(
        title=_(u"Posture"),
        vocabulary='vocabulary.posture',
        required=False,
    )

    directives.widget(gender=RadioFieldWidget)
    gender = schema.Choice(
        title=_(u"Gender"),
        vocabulary='vocabulary.gender',
        required=False,
    )
    shi_d = schema.TextLine(
        title=_(u"ShiZi Depth"),
        required=False,
    )
    shi_w = schema.TextLine(
        title=_(u"ShiZi Width"),
        required=False,
    )
    shi_h = schema.TextLine(
        title=_(u"ShiZi Height"),
        required=False,
    )
    shi_t = schema.TextLine(
        title=_(u"ShiZi Head"),
        required=False,
    )
    base_l = schema.TextLine(
        title=_(u"Base Length"),
        required=False,
    )
    base_w = schema.TextLine(
        title=_(u"Base Width"),
        required=False,
    )
    base_h = schema.TextLine(
        title=_(u"Base Height"),
        required=False,
    )


class IPhoto(model.Schema):
    """Photo Type"""
    id = schema.TextLine(
        title=_(u"Code"),
	required=True,
	description =_(u"A String Based on Abbreviation of Administrative Area.")
    )
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    image = namedfile.NamedBlobImage(
        title=_(u"Image"),
    )
    category = schema.Tuple(
        title=_(u"Category"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.category',
        ),
        missing_value=()
    )
    attachesTo = schema.Tuple(
        title=_(u"Attached To"),
        required=False,
        value_type=schema.Choice(
          vocabulary='vocabulary.attachesTo',
        ),
        missing_value=()
    )
    cou = schema.TextLine(
        title=_(u"County"),
        required=False,
    )
    tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
    )
    vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
    )
    lng = schema.TextLine(
        title=_(u"Longtitude"),
        required=False,
    )
    lat = schema.TextLine(
        title=_(u"Latitude"),
        required=False,
    )
    year = schema.TextLine(
        title=_(u"Photo Year"),
        required=False,
    )
    month = schema.TextLine(
        title=_(u"Photo Month"),
        required=False,
    )
    day = schema.TextLine(
        title=_(u"Photo Day"),
        required=False,
    )
    owner_name = schema.TextLine(
        title=_(u"Owner Name"),
        required=False,
    )
    owner_org = schema.TextLine(
        title=_(u"Owner Organization"),
        required=False,
    )
    owner_title = schema.TextLine(
        title=_(u"Owner Title"),
        required=False,
    )
    reference = RichTextField(
        title=_(u"Reference"),
        required=False,
    )


class IPilgrimage(model.Schema):
    """Pilgrimage Type"""
    id = schema.TextLine(
        title=_(u"Code"),
	required=True,
	description =_(u"A String Based on Abbreviation of Administrative Area.")
    )
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    body = RichTextField(
        title=_(u"Body"),
        required=False,
    )


class ISchedule(model.Schema):
    """Schedule Type"""
    id = schema.TextLine(
        title=_(u"Code"),
	required=True,
	description =_(u"A String Based on Abbreviation of Administrative Area.")
    )
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
    body = RichTextField(
        title=_(u"Body"),
        required=False,
    )
    temples = RelationList(
        title=_(u"Related Temples"),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=u"Related Temple",
            source=CatalogSource(portal_type='Temple')
        ),
    )

