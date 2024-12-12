from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod


class RouteActionPointRequiredAction(Enum):
    """
    RouteActionPointRequiredAction should be used to inform the required action of
    the route action point.

    :cvar VALUE_1: UserDefined
    :cvar VALUE_2: Report
    :cvar VALUE_3: UKCM
    :cvar VALUE_4: Note
    :cvar VALUE_5: Warning raised on ECDIS
    :cvar VALUE_6: Reserved
    :cvar VALUE_7: Reserved
    :cvar VALUE_8: Reserved
    :cvar VALUE_9: Reserved
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class RouteInfoStatus(Enum):
    """
    RouteStatusInfo should be used to inform the status of the route information.

    :cvar VALUE_1: Initial
    :cvar VALUE_2: Planned
    :cvar VALUE_3: Recommended
    :cvar VALUE_4: Acknowledged
    :cvar VALUE_5: Used for Monitoring
    :cvar VALUE_6: Terminated
    :cvar VALUE_7: Errors
    :cvar VALUE_8: Incomplete
    :cvar VALUE_9: Route issues
    :cvar VALUE_10: Service started
    :cvar VALUE_11: Service ended
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11


class RouteInfoVesselType(Enum):
    """
    Vessel Type.

    :cvar VALUE_0: Fishing
    :cvar VALUE_1: Towing
    :cvar VALUE_3: Engaged in dredging or underwater operations
    :cvar VALUE_4: Engaged in diving operations
    :cvar VALUE_5: Engaged in diving operations
    :cvar VALUE_6: Sailing
    :cvar VALUE_7: Plaeasure craft
    :cvar VALUE_8: Reserved for future use
    :cvar VALUE_9: Reserved for future use
    :cvar VALUE_10: 1-Reserved for future use, 0-All ships of this type
    :cvar VALUE_21: 2-WIG, 1-Carrying DG, HS MP, IMO Hazard or pollutant
        category X(2)
    :cvar VALUE_32: 3-See right column 2-WIG, 1-Carrying DG, HS MP, IMO
        Hazard or pollutant category Y(2)
    :cvar VALUE_43: 4-HSC 3-Carrying DG, HS MP, IMO Hazard or pollutant
        category OS(2)
    :cvar VALUE_50: Pilot vessel
    :cvar VALUE_51: Search and Rescue Vessel
    :cvar VALUE_52: Tugs
    :cvar VALUE_53: Port tenders
    :cvar VALUE_54: vessel with anti-pollution facilities and equipment
    :cvar VALUE_55: Law enforcement vessels
    :cvar VALUE_56: Spare - for assignments to local vessels
    :cvar VALUE_57: Spare 2 - for assignments to local vessels
    :cvar VALUE_58: Medical transports
    :cvar VALUE_59: Ships and aircraft of States not parties to an armed
        conflict
    :cvar VALUE_66: 6-Passenger ships, 6-Reserved for future use
    :cvar VALUE_77: 7-Cargo ships, 7-Reserved for future use
    :cvar VALUE_88: 8-Tankers, 8-Reserved for future use
    :cvar VALUE_99: 1-Other ships of Ship, 9- No additional information
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_21 = 21
    VALUE_32 = 32
    VALUE_43 = 43
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_66 = 66
    VALUE_77 = 77
    VALUE_88 = 88
    VALUE_99 = 99


class RouteScheduleElementType(Enum):
    MANUAL = "manual"
    CALCULATED = "calculated"
    RECOMMENDED = "recommended"
    ACTUAL = "actual"


class RouteWaypointLegGeometryType(Enum):
    """
    RL/GC indicator.

    :cvar VALUE_1: Loxodrome
    :cvar VALUE_2: Orthodrome
    """

    VALUE_1 = 1
    VALUE_2 = 2


class MdTopicCategoryCode(Enum):
    """Topic categories in S-100 Edition 1.0.0 and gmxCodelists.xml from OGC ISO 19139 XML schemas - see MD_TopicCategoryCode.
    Alternatives to this enumeration: (1) Add the ISO 19139 schemas to this profile and use the codelist MD_TopicCategoryCode instead.
    (2) Ise numeric codes for literals instead of labels, e.g., "1" instead of "farming".

    :cvar FARMING: rearing of animals and/or cultivation of plants.
        Examples: agriculture, irrigation, aquaculture, plantations,
        herding, pests and diseases affecting crops and livestock
    :cvar BIOTA: flora and/or fauna in natural environment. Examples:
        wildlife, vegetation, biological sciences, ecology, wilderness,
        sealife, wetlands, habitat
    :cvar BOUNDARIES: legal land descriptions. Examples: political and
        administrative boundaries
    :cvar CLIMATOLOGY_METEOROLOGY_ATMOSPHERE: processes and phenomena of
        the atmosphere. Examples: cloud cover, weather, climate,
        atmospheric conditions, climate change, precipitation
    :cvar ECONOMY: economic activities, conditions and employment.
        Examples: production, labour, revenue, commerce, industry,
        tourism and ecotourism, forestry, fisheries, commercial or
        subsistence hunting, exploration and exploitation of resources
        such as minerals, oil and gas
    :cvar ELEVATION: height above or below sea level. Examples:
        altitude, bathymetry, digital elevation models, slope, derived
        products
    :cvar ENVIRONMENT: environmental resources, protection and
        conservation. Examples: environmental pollution, waste storage
        and treatment, environmental impact assessment, monitoring
        environmental risk, nature reserves, landscape
    :cvar GEOSCIENTIFIC_INFORMATION: information pertaining to earth
        sciences. Examples: geophysical features and processes, geology,
        minerals, sciences dealing with the composition, structure and
        origin of the earth s rocks, risks of earthquakes, volcanic
        activity, landslides, gravity information, soils, permafrost,
        hydrogeology, erosion
    :cvar HEALTH: health, health services, human ecology, and safety.
        Examples: disease and illness, factors affecting health,
        hygiene, substance abuse, mental and physical health, health
        services
    :cvar IMAGERY_BASE_MAPS_EARTH_COVER: base maps. Examples: land
        cover, topographic maps, imagery, unclassified images,
        annotations
    :cvar INTELLIGENCE_MILITARY: military bases, structures, activities.
        Examples: barracks, training grounds, military transportation,
        information collection
    :cvar INLAND_WATERS: inland water features, drainage systems and
        their characteristics. Examples: rivers and glaciers, salt
        lakes, water utilization plans, dams, currents, floods, water
        quality, hydrographic charts
    :cvar LOCATION: positional information and services. Examples:
        addresses, geodetic networks, control points, postal zones and
        services, place names
    :cvar OCEANS: features and characteristics of salt water bodies
        (excluding inland waters). Examples: tides, tidal waves, coastal
        information, reefs
    :cvar PLANNING_CADASTRE: information used for appropriate actions
        for future use of the land. Examples: land use maps, zoning
        maps, cadastral surveys, land ownership
    :cvar SOCIETY: characteristics of society and cultures. Examples:
        settlements, anthropology, archaeology, education, traditional
        beliefs, manners and customs, demographic data, recreational
        areas and activities, social impact assessments, crime and
        justice, census information
    :cvar STRUCTURE: man-made construction. Examples: buildings,
        museums, churches, factories, housing, monuments, shops, towers
    :cvar TRANSPORTATION: means and aids for conveying persons and/or
        goods. Examples: roads, airports/airstrips, shipping routes,
        tunnels, nautical charts, vehicle or vessel location,
        aeronautical charts, railways
    :cvar UTILITIES_COMMUNICATION: energy, water and waste systems and
        communications infrastructure and services. Examples:
        hydroelectricity, geothermal, solar and nuclear sources of
        energy, water purification and distribution, sewage collection
        and disposal, electricity and gas distribution, data
        communication, telecommunication, radio, communication networks
    """

    FARMING = "farming"
    BIOTA = "biota"
    BOUNDARIES = "boundaries"
    CLIMATOLOGY_METEOROLOGY_ATMOSPHERE = "climatologyMeteorologyAtmosphere"
    ECONOMY = "economy"
    ELEVATION = "elevation"
    ENVIRONMENT = "environment"
    GEOSCIENTIFIC_INFORMATION = "geoscientificInformation"
    HEALTH = "health"
    IMAGERY_BASE_MAPS_EARTH_COVER = "imageryBaseMapsEarthCover"
    INTELLIGENCE_MILITARY = "intelligenceMilitary"
    INLAND_WATERS = "inlandWaters"
    LOCATION = "location"
    OCEANS = "oceans"
    PLANNING_CADASTRE = "planningCadastre"
    SOCIETY = "society"
    STRUCTURE = "structure"
    TRANSPORTATION = "transportation"
    UTILITIES_COMMUNICATION = "utilitiesCommunication"


class S100CircleByCenterPointTypeAngularDistance(Enum):
    VALUE_360_0 = Decimal("360.0")
    VALUE_360_0_1 = Decimal("-360.0")


@dataclass
class S100GmKnotType:
    """
    S-100 Knot is the GML 3.2.1 definition of Knot with the erroneous "weight"
    element removed.
    """

    class Meta:
        name = "S100_GM_KnotType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    multiplicity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )


class S100GmKnotTypeType(Enum):
    """This enumeration type specifies values for the knots' type (see ISO
    19107:2003, 6.4.25).

    The S-100 3.1 type extends it with "nonUniform" in keeping with the
    2017 draft of 19107

    :cvar UNIFORM: knots are equally spaced, all multiplicity 1
    :cvar QUASI_UNIFORM: the interior knots are uniform, but the first
        and last have multiplicity one larger than the degree of the
        spline
    :cvar PIECEWISE_BEZIER: the underlying spline is formally a Bézier
        spline, but knot multiplicity is always the degree of the spline
        except at the ends where the knot degree is (p+1). Such a spline
        is a pure Bézier spline between its distinct knots
    :cvar NON_UNIFORM: knots have varying spacing and multiplicity
    """

    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"
    NON_UNIFORM = "nonUniform"


@dataclass
class S100TruncatedDate:
    """
    Built in date types from W3C XML schema, implementing S-100 truncated date.
    """

    class Meta:
        name = "S100_TruncatedDate"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    g_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gDay",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    g_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonth",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    g_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYear",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    g_month_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonthDay",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    g_year_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYearMonth",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


class ComplianceLevelValue(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class DatasetPurposeType(Enum):
    """
    New type introduced in S-100 Ed 5 to distinguish between a Base dataset and an
    Update.

    :cvar BASE: rearing of animals and/or cultivation of plants.
        Examples: agriculture, irrigation, aquaculture, plantations,
        herding, pests and diseases affecting crops and livestock
    :cvar UPDATE: flora and/or fauna in natural environment. Examples:
        wildlife, vegetation, biological sciences, ecology, wilderness,
        sealife, wetlands, habitat
    """

    BASE = "base"
    UPDATE = "update"


@dataclass
class AbstractCurveSegmentType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    num_derivatives_at_start: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtStart",
            "type": "Attribute",
        },
    )
    num_derivatives_at_end: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtEnd",
            "type": "Attribute",
        },
    )
    num_derivative_interior_attribute: int = field(
        default=0,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Attribute",
        },
    )


@dataclass
class AbstractFeatureMemberType:
    """To create a collection of GML features, a property type shall be derived by
    extension from gml:AbstractFeatureMemberType.

    By default, this abstract property type does not imply any ownership
    of the features in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of a feature in the collection. A
    collection shall not own a feature already owned by another object.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class AbstractMemberType:
    """To create a collection of GML Objects that are not all features, a property
    type shall be derived by extension from gml:AbstractMemberType.

    This abstract property type is intended to be used only in object
    types where software shall be able to identify that an instance of
    such an object type is to be interpreted as a collection of objects.
    By default, this abstract property type does not imply any ownership
    of the objects in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of an object in the collection. A
    collection shall not own an object already owned by another object.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractMetadataPropertyType:
    """To associate metadata described by any XML Schema with a GML object, a
    property element shall be defined whose content model is derived by extension
    from gml:AbstractMetadataPropertyType.

    The value of such a property shall be metadata. The content model of
    such a property type, i.e. the metadata application schema shall be
    specified by the GML Application Schema. By default, this abstract
    property type does not imply any ownership of the metadata. The owns
    attribute of gml:OwnershipAttributeGroup may be used on a metadata
    property element instance to assert ownership of the metadata. If
    metadata following the conceptual model of ISO 19115 is to be
    encoded in a GML document, the corresponding Implementation
    Specification specified in ISO/TS 19139 shall be used to encode the
    metadata information.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractObject:
    """This element has no type defined, and is therefore implicitly (according to
    the rules of W3C XML Schema) an XML Schema anyType.

    It is used as the head of an XML Schema substitution group which
    unifies complex content and certain simple content elements used for
    datatypes in GML, including the gml:AbstractGML substitution group.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRingType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractScalarValue:
    """
    Gml:AbstractScalarValue is an abstract element which acts as the head of a
    substitution group which contains gml:Boolean, gml:Category, gml:Count and
    gml:Quantity, and (transitively) the elements in their substitution groups.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AbstractSurfacePatchType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractValue:
    """Gml:AbstractValue is an abstract element which acts as the head of a
    substitution group which contains gml:AbstractScalarValue,
    gml:AbstractScalarValueList, gml:CompositeValue and gml:ValueExtent, and
    (transitively) the elements in their substitution groups.

    These elements may be used in an application schema as variables, so
    that in an XML instance document any member of its substitution
    group may occur.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class AggregationType(Enum):
    SET = "set"
    BAG = "bag"
    SEQUENCE = "sequence"
    ARRAY = "array"
    RECORD = "record"
    TABLE = "table"


@dataclass
class CodeType:
    """Gml:CodeType is a generalized type to be used for a term, keyword or name.

    It adds a XML attribute codeSpace to a term, where the value of the
    codeSpace attribute (if present) shall indicate a dictionary,
    thesaurus, classification scheme, authority, or pattern for the
    term.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )


class CurveInterpolationType(Enum):
    """Gml:CurveInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an applicationschema.

    S-100 3.1 note: The list has been extended by adding the S-100 3.1
    interpolations, given that the new draft of ISO 19107 explicitly
    says "As a codelist, there is no intention of limiting the potential
    values ofCurveInterpolation."

    :cvar NONE:
    :cvar LINEAR:
    :cvar GEODESIC:
    :cvar CIRCULAR_ARC3_POINTS:
    :cvar LOXODROMIC: Note that the new draft of 19107 now includes
        "rhumb".
    :cvar ELLIPTICAL:
    :cvar CONIC:
    :cvar CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS:
    :cvar POLYNOMIAL_SPLINE:
    :cvar BEZIER_SPLINE:
    :cvar B_SPLINE:
    :cvar CUBIC_SPLINE:
    :cvar RATIONAL_SPLINE:
    :cvar BLENDED_PARABOLIC:
    """

    NONE = "none"
    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    LOXODROMIC = "loxodromic"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    BEZIER_SPLINE = "bezierSpline"
    B_SPLINE = "bSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"
    BLENDED_PARABOLIC = "blendedParabolic"


@dataclass
class DirectPositionListType:
    """PosList instances (and other instances with the content model specified by
    DirectPositionListType) hold the coordinates for a sequence of direct positions
    within the same coordinate reference system (CRS).

    if no srsName attribute is given, the CRS shall be specified as part
    of the larger context this geometry element is part of, typically a
    geometric object like a point, curve, etc. The optional attribute
    count specifies the number of direct positions in the list. If the
    attribute count is present then the attribute srsDimension shall be
    present, too. The number of entries in the list is equal to the
    product of the dimensionality of the coordinate reference system
    (i.e. it is a derived value of the coordinate reference system
    definition) and the number of direct positions.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DirectPositionType:
    """Direct position instances hold the coordinates for a position within some
    coordinate reference system (CRS).

    Since direct positions, as data types, will often be included in
    larger objects (such as geometry elements) that have references to
    CRS, the srsName attribute will in general be missing, if this
    particular direct position is included in a larger element with such
    a reference to a CRS. In this case, the CRS is implicitly assumed to
    take on the value of the containing object's CRS. if no srsName
    attribute is given, the CRS shall be specified as part of the larger
    context this geometry element is part of, typically a geometric
    object like a point, curve, etc.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )


@dataclass
class InlinePropertyType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MeasureType:
    """Gml:MeasureType supports recording an amount encoded as a value of XML
    Schema double, together with a units of measure indicated by an attribute uom,
    short for "units Of measure".

    The value of the uom attribute identifies a reference system for the
    amount, usually a ratio or interval scale.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: /n/r/t]+",
        },
    )


class NilReasonEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"


class SignType(Enum):
    """
    Gml:SignType is a convenience type with values "+" (plus) and "-" (minus).
    """

    HYPHEN_MINUS = "-"
    PLUS_SIGN = "+"


class SurfaceInterpolationType(Enum):
    """
    Gml:SurfaceInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an application schema.
    """

    NONE = "none"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    TIN = "tin"
    PARAMETRIC_CURVE = "parametricCurve"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    RATIONAL_SPLINE = "rationalSpline"
    TRIANGULATED_SPLINE = "triangulatedSpline"


@dataclass
class AssociationName:
    class Meta:
        name = "associationName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DefaultCodeSpace:
    class Meta:
        name = "defaultCodeSpace"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class GmlProfileSchema:
    class Meta:
        name = "gmlProfileSchema"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ReversePropertyName:
    """If the value of an object property is another object and that object
    contains also a property for the association between the two objects, then this
    name of the reverse property may be encoded in a gml:reversePropertyName
    element in an appinfo annotation of the property element to document the
    constraint between the two properties.

    The value of the element shall contain the qualified name of the
    property element.
    """

    class Meta:
        name = "reversePropertyName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class TargetElement:
    class Meta:
        name = "targetElement"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ActuateType(Enum):
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE = "none"


class ShowType(Enum):
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE = "none"


class TypeType(Enum):
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"


class LangValue(Enum):
    VALUE = ""


@dataclass
class AbstractAttributeType(AbstractGmltype):
    """
    Abstract type for attributes.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class AbstractInformationType(AbstractGmltype):
    """Abstract type for an S-100 information type.

    This is the base type from which domain application schemas derive
    definitions for their individual information types.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class DataSetIdentificationType:
    """S-100 Data Set Identification.

    The fields correspond to S-100 10a-5.1.2.1 fields. Attributes
    encodingSpecification and encodingSpecificationEdition are actually
    redundant here because in an XML schema the encoding specification
    and encoding specification edition are usually implicit in the
    namespace URI.

    :ivar encoding_specification: Encoding specification that defines
        the encoding.
    :ivar encoding_specification_edition: Edition of the encoding
        specification
    :ivar product_identifier: Unique identifier of the data product as
        specified in the product specification
    :ivar product_edition: Edition of the product specification
    :ivar application_profile: Identifier that specifies a profile
        within the data product
    :ivar dataset_file_identifier: The file identifier of the dataset
    :ivar dataset_title: The title of the dataset
    :ivar dataset_reference_date: The reference date of the dataset
    :ivar dataset_language: The (primary) language used in this dataset
    :ivar dataset_abstract: The abstract of the dataset
    :ivar dataset_topic_category: A set of topic categories
    :ivar dataset_purpose: base or update
    :ivar update_number: Update Number, 0 for a Base dataset
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    encoding_specification: str = field(
        init=False,
        default="S-100 Part 10b",
        metadata={
            "name": "encodingSpecification",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    encoding_specification_edition: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "encodingSpecificationEdition",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    product_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "productIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    product_edition: Optional[str] = field(
        default=None,
        metadata={
            "name": "productEdition",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    application_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationProfile",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    dataset_file_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetFileIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    dataset_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetTitle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    dataset_reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datasetReferenceDate",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    dataset_language: str = field(
        default="eng",
        metadata={
            "name": "datasetLanguage",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
            "pattern": r"\w{3}",
        },
    )
    dataset_abstract: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetAbstract",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    dataset_topic_category: List[MdTopicCategoryCode] = field(
        default_factory=list,
        metadata={
            "name": "datasetTopicCategory",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "min_occurs": 1,
        },
    )
    dataset_purpose: Optional[DatasetPurposeType] = field(
        default=None,
        metadata={
            "name": "datasetPurpose",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    update_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "updateNumber",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )


@dataclass
class KnotPropertyType:
    """Gml:KnotPropertyType encapsulates a knot to use it in a geometric type.

    The S100 version is needed so as to use the updated definition of
    knots

    :ivar knot: A knot is a breakpoint on a piecewise spline curve.
        value is the value of the parameter at the knot of the spline
        (see ISO 19107:2003, 6.4.24.2). multiplicity is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight). weight is the value of the averaging weight used for
        this knot of the spline.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    knot: Optional[S100GmKnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )


@dataclass
class ComplianceLevel:
    """
    Level 1 = Level 2 =
    """

    class Meta:
        name = "complianceLevel"
        namespace = "http://www.iho.int/s100gml/5.0"

    value: Optional[ComplianceLevelValue] = field(default=None)


@dataclass
class AbstractCurveSegment(AbstractCurveSegmentType):
    """A curve segment defines a homogeneous segment of a curve.

    The attributes numDerivativesAtStart, numDerivativesAtEnd and
    numDerivativesInterior specify the type of continuity as specified
    in ISO 19107:2003, 6.4.9.3. The AbstractCurveSegment element is the
    abstract head of the substituition group for all curve segment
    elements, i.e. continuous segments of the same interpolation
    mechanism. All curve segments shall have an attribute interpolation
    with type gml:CurveInterpolationType specifying the curve
    interpolation mechanism used for this segment. This mechanism uses
    the control points and control parameters to determine the position
    of this curve segment.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGml(AbstractGmltype):
    """The abstract element gml:AbstractGML is "any GML object having identity".

    It acts as the head of an XML Schema substitution group, which may
    include any element which is a GML feature, or other object, with
    identity. This is used as a variable in content models in GML core
    and application schemas. It is effectively an abstract superclass
    for all GML objects.
    """

    class Meta:
        name = "AbstractGML"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometryType(AbstractGmltype):
    """All geometry elements are derived directly or indirectly from this abstract
    supertype. A geometry element may have an identifying attribute (gml:id), one
    or more names (elements identifier and name) and a description (elements
    description and descriptionReference) . It may be associated with a spatial.

    reference system (attribute group gml:SRSReferenceGroup). The following rules shall
    be adhered to: - Every geometry type shall derive from this abstract type. - Every
    geometry element (i.e. an element of a geometry type) shall be directly or
    indirectly in the substitution group of AbstractGeometry.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )


@dataclass
class AbstractRing(AbstractRingType):
    """An abstraction of a ring to support surface boundaries of different
    complexity.

    The AbstractRing element is the abstract head of the substituition
    group for all closed boundaries of a surface patch.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurfacePatch(AbstractSurfacePatchType):
    """A surface patch defines a homogenuous portion of a surface.

    The AbstractSurfacePatch element is the abstract head of the
    substituition group for all surface patch elements describing a
    continuous portion of a surface. All surface patches shall have an
    attribute interpolation (declared in the types derived from
    gml:AbstractSurfacePatchType) specifying the interpolation mechanism
    used for the patch using gml:SurfaceInterpolationType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AngleType(MeasureType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AssociationRoleType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class Boolean:
    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class CodeWithAuthorityType(CodeType):
    """
    Gml:CodeWithAuthorityType requires that the codeSpace attribute is provided in
    an instance.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EnvelopeType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    lower_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    upper_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )


@dataclass
class FeaturePropertyType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class LengthType(MeasureType):
    """This is a prototypical definition for a specific measure type defined as a
    vacuous extension (i.e. aliases) of gml:MeasureType.

    In this case, the content model supports the description of a length
    (or distance) quantity, with its units. The unit of measure
    referenced by uom shall be suitable for a length, such as metres or
    feet.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ReferenceType:
    """
    Gml:ReferenceType is intended to be used in application schemas directly, if a
    property element shall use a "by-reference only" encoding.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class VolumeType(MeasureType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractInlineProperty(InlinePropertyType):
    """
    Gml:abstractInlineProperty may be used as the head of a subtitution group of
    more specific elements providing a value inline.
    """

    class Meta:
        name = "abstractInlineProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Measure(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """

    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcType:
    """
    :ivar type_value:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar from_value:
    :ivar to: from and to have default behavior when values are missing
    """

    class Meta:
        name = "arcType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.ARC,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class Extended:
    """Intended for use as the type of user-declared elements to make them extended
    links.

    Note that the elements referenced in the content model are all
    abstract. The intention is that by simply declaring elements with
    these as their substitutionGroup, all the right things will happen.
    """

    class Meta:
        name = "extended"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.EXTENDED,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class LocatorType:
    """
    :ivar type_value:
    :ivar href:
    :ivar role:
    :ivar title:
    :ivar label: label is not required, but locators have no particular
        XLink function if they are not labeled.
    """

    class Meta:
        name = "locatorType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.LOCATOR,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class ResourceType:
    class Meta:
        name = "resourceType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.RESOURCE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Simple:
    """
    Intended for use as the type of user-declared elements to make them simple
    links.
    """

    class Meta:
        name = "simple"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class TitleEltType:
    """
    :ivar type_value:
    :ivar lang: xml:lang is not required, but provides much of the
        motivation for title elements in addition to attributes, and so
        is provided here for convenience.
    :ivar content:
    """

    class Meta:
        name = "titleEltType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type_value: TypeType = field(
        init=False,
        default=TypeType.TITLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class RouteExtensions(AbstractInformationType):
    """
    Route Extensions.

    :ivar route_extensions_note: Route Extension Note
    :ivar any_element:
    :ivar route_extensions_manufacturer_id: Unique vendor identifier for
        the Route extensions
    :ivar route_extensions_name: Route extension name
    :ivar route_extensions_version: RouteExtension version
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_extensions_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeExtensionsNote",
            "type": "Element",
            "namespace": "",
        },
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    route_extensions_manufacturer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeExtensionsManufacturerId",
            "type": "Attribute",
            "required": True,
        },
    )
    route_extensions_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeExtensionsName",
            "type": "Attribute",
        },
    )
    route_extensions_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeExtensionsVersion",
            "type": "Attribute",
        },
    )


@dataclass
class S100SpatialAttributeType:
    """
    S-100 Base type for the geometry of a feature.
    """

    class Meta:
        name = "S100_SpatialAttributeType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    mask_reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "maskReference",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )
    scale_minimum: Optional[int] = field(
        default=None,
        metadata={
            "name": "scaleMinimum",
            "type": "Attribute",
        },
    )
    scale_maximum: Optional[int] = field(
        default=None,
        metadata={
            "name": "scaleMaximum",
            "type": "Attribute",
        },
    )


@dataclass
class InformationAssociation(ReferenceType):
    class Meta:
        name = "informationAssociation"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    """Gml:AbstractGeometricPrimitiveType is the abstract root type of the
    geometric primitives.

    A geometric primitive is a geometric object that is not decomposed
    further into other primitives in the system. All primitives are
    oriented in the direction implied by the sequence of their
    coordinate tuples.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometry(AbstractGeometryType):
    """The AbstractGeometry element is the abstract head of the substitution group
    for all geometry elements of GML.

    This includes pre-defined and user-defined geometry elements. Any
    geometry element shall be a direct or indirect extension/restriction
    of AbstractGeometryType and shall be directly or indirectly in the
    substitution group of AbstractGeometry.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Envelope(EnvelopeType):
    """Envelope defines an extent using a pair of positions defining opposite
    corners in arbitrary dimensions.

    The first direct position is the "lower corner" (a coordinate
    position consisting of all the minimal ordinates for each dimension
    for all points within the envelope), the second one the "upper
    corner" (a coordinate position consisting of all the maximal
    ordinates for each dimension for all points within the envelope).
    The use of the properties "coordinates" and "pos" has been
    deprecated. The explicitly named properties "lowerCorner" and
    "upperCorner" shall be used instead.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractAssociationRole(AssociationRoleType):
    """Applying this pattern shall restrict the multiplicity of objects in a
    property element using this content model to exactly one. An instance of this
    type shall contain an element representing an object, or serve as a pointer to
    a remote.

    object. Applying the pattern to define an application schema specific property type
    allows to restrict - the inline object to specified object types, - the encoding to
    "by-reference only" (see 7.2.3.7), - the encoding to "inline only" (see 7.2.3.8).
    """

    class Meta:
        name = "abstractAssociationRole"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractReference(ReferenceType):
    """
    Gml:abstractReference may be used as the head of a subtitution group of more
    specific elements providing a value by-reference.
    """

    class Meta:
        name = "abstractReference"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Angle(AngleType):
    """
    The gml:angle property element is used to record the value of an angle quantity
    as a single number, with its units.
    """

    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Arc(ArcType):
    class Meta:
        name = "arc"
        namespace = "http://www.w3.org/1999/xlink"


@dataclass
class Locator(LocatorType):
    class Meta:
        name = "locator"
        namespace = "http://www.w3.org/1999/xlink"


@dataclass
class Resource(ResourceType):
    class Meta:
        name = "resource"
        namespace = "http://www.w3.org/1999/xlink"


@dataclass
class Title(TitleEltType):
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/1999/xlink"


@dataclass
class RouteInfo(AbstractInformationType):
    """
    List of route information.

    :ivar route_info_name: Name of the route, At least three characters
        of alphanumeric and periods. The first and last letters are
        alphanumeric only
    :ivar route_info_author: Author of the route
    :ivar route_info_description: Additional information for the status
        of the route i.e. specific error message and/or cause of the
        route change and/or any other detail to consider before futher
        use of this route plan and/or the purpose of sending a route
        plan and/or why this route is recommended.
    :ivar route_info_departure_port_id2: Secondary identifier for
        departure port given by free text string
    :ivar route_info_arrival_port_id2: Secondary identifier for arrival
        port given by free text string
    :ivar route_info_vessel_name: Ship’s name
    :ivar route_info_vessel_callsign: Ship’s Call sign
    :ivar route_info_extensions: Additional proprietary information for
        the route info specified by the manufacturer
    :ivar route_info_edition_time:
    :ivar route_info_status:
    :ivar route_info_validity_start:
    :ivar route_info_validity_end:
    :ivar route_info_departure_port_id1: Primary identifier for
        departure port given by UN/LOCODE
    :ivar route_info_departure_port_call: Reference to port call
        identifier in departinng port
    :ivar route_info_arrival_port_id1: Primary identifier for arrival
        port given by UN/LOCODE
    :ivar route_info_arrival_port_call: Reference to port call
        identifier in arriving port
    :ivar route_info_reference_prev_route: Reference previous route.
    :ivar route_info_reference_next_route: Reference Next route.
    :ivar route_info_vessel_type: Type of vessel
    :ivar route_info_vessel_mmsi: Ship’s MMSI (XXXXXXXXX)
    :ivar route_info_vessel_imo: Ship’s IMO number (XXXXXXX)
    :ivar route_info_vessel_voyage: Unique voyage identifier
    :ivar route_info_vessel_height: Vessel height measured from the keel
        to the masthead
    :ivar route_info_vessel_length: Vessel length overall (LOA)
    :ivar route_info_vessel_beam: Vessel beam
    :ivar route_info_draft_max: Maximum vessel draft
    :ivar route_info_air_draft_max: Maximum vessel air draft
    :ivar route_info_beam_max: Maximum Vessel beam
    :ivar route_info_length_max: Maximum Vessel length
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_info_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"([a-zA-Z|\d]+[a-zA-Z|\d|W.|\s|W_|W-]+[a-zA-Z|\d])",
        },
    )
    route_info_author: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoAuthor",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoDescription",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_departure_port_id2: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoDeparturePortID2",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_arrival_port_id2: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoArrivalPortID2",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_vessel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselName",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_vessel_callsign: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselCallsign",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeInfoExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_info_edition_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "routeInfoEditionTime",
            "type": "Attribute",
        },
    )
    route_info_status: Optional[RouteInfoStatus] = field(
        default=None,
        metadata={
            "name": "routeInfoStatus",
            "type": "Attribute",
            "required": True,
        },
    )
    route_info_validity_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "routeInfoValidityStart",
            "type": "Attribute",
        },
    )
    route_info_validity_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "routeInfoValidityEnd",
            "type": "Attribute",
        },
    )
    route_info_departure_port_id1: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoDeparturePortID1",
            "type": "Attribute",
            "length": 5,
            "pattern": r"[a-zA-Z]{5}",
        },
    )
    route_info_departure_port_call: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoDeparturePortCall",
            "type": "Attribute",
        },
    )
    route_info_arrival_port_id1: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoArrivalPortID1",
            "type": "Attribute",
            "length": 5,
            "pattern": r"[a-zA-Z]{5}",
        },
    )
    route_info_arrival_port_call: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoArrivalPortCall",
            "type": "Attribute",
        },
    )
    route_info_reference_prev_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoReferencePrevRoute",
            "type": "Attribute",
        },
    )
    route_info_reference_next_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoReferenceNextRoute",
            "type": "Attribute",
        },
    )
    route_info_vessel_type: Optional[RouteInfoVesselType] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselType",
            "type": "Attribute",
        },
    )
    route_info_vessel_mmsi: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselMMSI",
            "type": "Attribute",
            "length": 9,
            "pattern": r"\d{9}",
        },
    )
    route_info_vessel_imo: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselIMO",
            "type": "Attribute",
            "length": 7,
            "pattern": r"\d{7}",
        },
    )
    route_info_vessel_voyage: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselVoyage",
            "type": "Attribute",
        },
    )
    route_info_vessel_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselHeight",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_vessel_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselLength",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_vessel_beam: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoVesselBeam",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_draft_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoDraftMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_air_draft_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoAirDraftMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_beam_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoBeamMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_info_length_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeInfoLengthMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )


@dataclass
class RouteScheduleElement(AbstractInformationType):
    """
    :ivar route_schedule_element_note: Notes for the route schedule
        element
    :ivar route_schedule_element_extensions: Additional proprietary
        information for the route schedules specified by the
        manufacturer
    :ivar route_schedule_element_type: Defines the type of the schedule
        element. Can be used to generate the list of different types of
        schedule elements if required.
    :ivar route_schedule_element_plan_sog: Planned speed over ground
    :ivar route_schedule_element_etd: Planned  or Recommended Time of
        departure represented by Estimated Time of departure (ETD)
    :ivar route_schedule_element_eta: Planned or Recommended Time of
        arrival represented by Estimated time of arrival (ETA)
    :ivar route_schedule_element_etdwindow_before: Describes the
        uncertainty of the predicted ETD before planned time or
        recommended time
    :ivar route_schedule_element_etdwindow_after: Describes the
        uncertainty of the predicted ETD after planned time or
        recommended time
    :ivar route_schedule_element_etawindow_before: Describes the
        uncertainty of the predicted ETA before planned time or
        recommended time
    :ivar route_schedule_element_etawindow_after: Describes the
        uncertainty of the predicted ETA after planned time or
        recommended time
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_schedule_element_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementNote",
            "type": "Element",
            "namespace": "",
        },
    )
    route_schedule_element_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeScheduleElementExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_schedule_element_type: Optional[RouteScheduleElementType] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementType",
            "type": "Attribute",
            "required": True,
        },
    )
    route_schedule_element_plan_sog: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementPlanSOG",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    route_schedule_element_etd: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETD",
            "type": "Attribute",
        },
    )
    route_schedule_element_eta: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETA",
            "type": "Attribute",
        },
    )
    route_schedule_element_etdwindow_before: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETDWindowBefore",
            "type": "Attribute",
        },
    )
    route_schedule_element_etdwindow_after: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETDWindowAfter",
            "type": "Attribute",
        },
    )
    route_schedule_element_etawindow_before: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETAWindowBefore",
            "type": "Attribute",
        },
    )
    route_schedule_element_etawindow_after: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeScheduleElementETAWindowAfter",
            "type": "Attribute",
        },
    )


@dataclass
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """Gml:AbstractCurveType is an abstraction of a curve to support the different
    levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregate(AbstractGeometricAggregateType):
    """
    Gml:AbstractGeometricAggregate is the abstract head of the substitution group
    for all geometric aggregates.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricPrimitive(AbstractGeometricPrimitiveType):
    """
    The AbstractGeometricPrimitive element is the abstract head of the substitution
    group for all (pre- and user-defined) geometric primitives.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """Gml:AbstractSurfaceType is an abstraction of a surface to support the
    different levels of complexity.

    A surface is always a continuous region of a plane.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundingShapeType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class PointType1(AbstractGeometricPrimitiveType):
    """S-100 XML supports two different ways to specify the direct positon of a
    point.

    1. The "pos" element is of type DirectPositionType.
    """

    class Meta:
        name = "PointType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class PointType2(PointType1):
    """
    S-100 point type adds an information association to the GML spatial type Point.
    """

    class Meta:
        name = "PointType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class AbstractCurve(AbstractCurveType):
    """
    The AbstractCurve element is the abstract head of the substitution group for
    all (continuous) curve elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurface(AbstractSurfaceType):
    """
    The AbstractSurface element is the abstract head of the substitution group for
    all (continuous) surface elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Point1(PointType1):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """

    class Meta:
        name = "Point"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundedBy(BoundingShapeType):
    """
    This property describes the minimum bounding box or rectangle that encloses the
    entire feature.
    """

    class Meta:
        name = "boundedBy"
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GmPoint:
    class Meta:
        name = "GM_Point"
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    point: Optional[PointType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Point2(PointType2):
    class Meta:
        name = "Point"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class AbstractFeatureTypeAbstract(AbstractGmltype):
    """The basic feature model is given by the gml:AbstractFeatureType.

    The content model for gml:AbstractFeatureType adds two specific
    properties suitable for geographic features to the content model
    defined in gml:AbstractGMLType. The value of the gml:boundedBy
    property describes an envelope that encloses the entire feature
    instance, and is primarily useful for supporting rapid searching for
    features that occur in a particular location. The value of the
    gml:location property describes the extent, position or relative
    location of the feature.
    """

    class Meta:
        name = "AbstractFeatureType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )


@dataclass
class PointPropertyType1:
    """A property that has a point as its value domain may either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    class Meta:
        name = "PointPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractFeatureType(AbstractFeatureTypeAbstract):
    """Abstract type for an S-100 feature.

    This is the base type from which domain application schemas derive
    definitions for their individual features. It derives from GML
    AbstractFeatureType.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class PointPropertyType2(S100SpatialAttributeType):
    """
    Point property using the S-100 point type.
    """

    class Meta:
        name = "PointPropertyType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class AbstractFeature(AbstractFeatureTypeAbstract):
    """This abstract element serves as the head of a substitution group which may
    contain any elements whose content model is derived from
    gml:AbstractFeatureType.

    This may be used as a variable in the construction of content
    models. gml:AbstractFeature may be thought of as "anything that is a
    GML feature" and may be used to define variables or templates in
    which the value of a GML property is "any feature". This occurs in
    particular in a GML feature collection where the feature member
    properties contain one or multiple copies of gml:AbstractFeature
    respectively.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointMember(PointPropertyType1):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """

    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointProperty1(PointPropertyType1):
    """This property element either references a point via the XLink-attributes or
    contains the point element.

    pointProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for Point.
    """

    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RouteActionPoint(AbstractFeatureType):
    """
    :ivar geometry: Geographical position of the action point in degrees
    :ivar route_action_point_name: Name of action point
    :ivar route_action_point_required_action_description: Human readable
        description of the action required for this action point
    :ivar route_action_point_extensions: Additional proprietary
        information for the action points specified by the manufacturer
    :ivar route_action_point_id: Identifier for the action point,
        variation of the name. Shall be unique for the route.
    :ivar route_action_point_external_reference: Machine readable
        external reference information related to the action point.
    :ivar route_action_point_radius: Distance from the action point
        within which action must be taken.
    :ivar route_action_point_time_to_act: Time before or after action
        point
    :ivar route_action_point_required_action: The action required for
        this action
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    geometry: Optional[GmPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    route_action_point_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeActionPointName",
            "type": "Element",
            "namespace": "",
        },
    )
    route_action_point_required_action_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeActionPointRequiredActionDescription",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    route_action_point_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeActionPointExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_action_point_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeActionPointID",
            "type": "Attribute",
        },
    )
    route_action_point_external_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeActionPointExternalReference",
            "type": "Attribute",
        },
    )
    route_action_point_radius: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeActionPointRadius",
            "type": "Attribute",
        },
    )
    route_action_point_time_to_act: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeActionPointTimeToAct",
            "type": "Attribute",
        },
    )
    route_action_point_required_action: Optional[
        RouteActionPointRequiredAction
    ] = field(
        default=None,
        metadata={
            "name": "routeActionPointRequiredAction",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RouteWaypointLeg(AbstractFeatureType):
    """
    :ivar route_waypoint_leg_note: Note for the route waypoint leg
    :ivar route_waypoint_leg_issue: Safety Issue for the route waypoint
        leg
    :ivar route_waypoint_leg_extensions: Additional proprietary
        information for the Route waypoint Legs specified by the
        manufacturer
    :ivar route_waypoint_leg_starboard_xtdl: Starboard cross track
        distance limit
    :ivar route_waypoint_leg_port_xtdl: Port cross track distance limit
    :ivar route_waypoint_leg_starboard_cl: Starboard cross track
        distance check limit
    :ivar route_waypoint_leg_port_cl: Port cross track distance check
        limit
    :ivar route_waypoint_leg_safety_contour: Planned safety contour
    :ivar route_waypoint_leg_safety_depth: Planned safety depth
    :ivar route_waypoint_leg_geometry_type: Geometry type of leg; 1:
        Loxodrome, 2: Orthodrome
    :ivar route_waypoint_leg_sogmin: Regulatory lowest speed over ground
    :ivar route_waypoint_leg_sogmax: Regulatory highest speed over
        ground
    :ivar route_waypoint_leg_stwmin: Minimum safe speed through water
    :ivar route_waypoint_leg_stwmax: Maximum safe speed through water
    :ivar route_waypoint_leg_draft: Planned static Draft, maximum
    :ivar route_waypoint_leg_draft_forward: Planned static Draft Forward
    :ivar route_waypoint_leg_draft_aft: Planned static Draft Aft
    :ivar route_waypoint_leg_draft_max: Maximum draft of the route
        waypoint leg for all vessles
    :ivar route_waypoint_leg_air_draft_max: Maximum air draft of the
        route waypoint leg for all vessels
    :ivar route_waypoint_leg_beam_max: Maximum vessel beam  of the route
        waypoint leg for all vessels
    :ivar route_waypoint_leg_length_max: Maximum vessel length  of the
        route waypoint leg for all vessels
    :ivar route_waypoint_leg_static_ukc: Minimum static UKC on the leg
    :ivar route_waypoint_leg_dynamic_ukc: Minimum dynamic UKC on the leg
    :ivar route_waypoint_leg_safety_margin: Draft component including
        uncertainties
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_waypoint_leg_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegNote",
            "type": "Element",
            "namespace": "",
        },
    )
    route_waypoint_leg_issue: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegIssue",
            "type": "Element",
            "namespace": "",
        },
    )
    route_waypoint_leg_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeWaypointLegExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_waypoint_leg_starboard_xtdl: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegStarboardXTDL",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 10000,
        },
    )
    route_waypoint_leg_port_xtdl: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegPortXTDL",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 10000,
        },
    )
    route_waypoint_leg_starboard_cl: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegStarboardCL",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 10000,
        },
    )
    route_waypoint_leg_port_cl: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegPortCL",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 10000,
        },
    )
    route_waypoint_leg_safety_contour: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSafetyContour",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_safety_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSafetyDepth",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_geometry_type: Optional[
        RouteWaypointLegGeometryType
    ] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegGeometryType",
            "type": "Attribute",
            "required": True,
        },
    )
    route_waypoint_leg_sogmin: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSOGMin",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    route_waypoint_leg_sogmax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSOGMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    route_waypoint_leg_stwmin: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSTWMin",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    route_waypoint_leg_stwmax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSTWMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    route_waypoint_leg_draft: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegDraft",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_draft_forward: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegDraftForward",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_draft_aft: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegDraftAft",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_draft_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegDraftMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_waypoint_leg_air_draft_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegAirDraftMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_waypoint_leg_beam_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegBeamMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_waypoint_leg_length_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegLengthMax",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 2,
        },
    )
    route_waypoint_leg_static_ukc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegStaticUKC",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )
    route_waypoint_leg_dynamic_ukc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegDynamicUKC",
            "type": "Attribute",
        },
    )
    route_waypoint_leg_safety_margin: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointLegSafetyMargin",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        },
    )


@dataclass
class S100ArcByCenterPointType(AbstractCurveSegmentType):
    """
    Type for S-100 arc by center point geometry.
    """

    class Meta:
        name = "S100_ArcByCenterPointType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: Optional[PointProperty1] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    radius: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    start_angle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        },
    )
    angular_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "angularDistance",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "min_inclusive": Decimal("-360.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class S100GmCurveType(AbstractCurveSegmentType):
    """<xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for curve segments with other interpolations</xs:documentation>"""

    class Meta:
        name = "S100_GM_CurveType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: Optional[CurveInterpolationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class S100GmSplineCurveType(AbstractCurveSegmentType):
    """<xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for general splines including b-splines</xs:documentation>"""

    class Meta:
        name = "S100_GM_SplineCurveType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    knot: List[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    knot_spec: Optional[S100GmKnotTypeType] = field(
        default=None,
        metadata={
            "name": "knotSpec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    is_rational: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "isRational",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
            "pattern": r"other:/w{2,}",
        },
    )
    interpolation: Optional[CurveInterpolationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VectorType:
    """
    Defintion of the Vector datatype used in splines.

    :ivar origin:
    :ivar dimension:
    :ivar offset: The number of values must be the same as "dimension"
        value
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    origin: Optional["VectorType.Origin"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )
    offset: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "tokens": True,
        },
    )

    @dataclass
    class Origin:
        pos: Optional[Pos] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            },
        )
        point_property: Optional[PointProperty1] = field(
            default=None,
            metadata={
                "name": "pointProperty",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            },
        )


@dataclass
class PointProperty2(PointPropertyType2):
    class Meta:
        name = "pointProperty"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class GeodesicStringType(AbstractCurveSegmentType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LineStringSegmentType(AbstractCurveSegmentType):
    """GML supports two different ways to specify the control points of a line
    string.

    1. A sequence of "pos" (DirectPositionType) or "pointProperty"
    (PointPropertyType) elements. "pos" elements are control points that are only part
    of this curve, "pointProperty" elements contain a point that may be referenced from
    other geometry elements or reference another point defined outside of this curve
    (reuse of existing points). 2. The "posList" element allows for a compact way to
    specifiy the coordinates of the control points, if all control points are in the
    same coordinate reference systems and belong to this curve only. The number of
    direct positions in the list must be at least two.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LineStringType(AbstractCurveType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class LinearRingType(AbstractRingType):
    """S-100 XML supports two different ways to specify the control points of a
    linear ring.

    1. A sequence of "pos" (DirectPositionType) or "pointProperty"
    (PointPropertyType) elements. "pos" elements are control points that are only part
    of this ring, "pointProperty" elements contain a point that may be referenced from
    other geometry elements or reference another point defined outside of this ring
    (reuse of existing points). 2. The "posList" element allows for a compact way to
    specifiy the coordinates of the control points, if all control points are in the
    same coordinate reference systems and belong to this ring only. The number of direct
    positions in the list must be at least four.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: List[PointProperty1] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class MultiPointType1(AbstractGeometricAggregateType):
    class Meta:
        name = "MultiPointType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class RouteActionPoints(AbstractFeatureType):
    """
    :ivar route_action_point:
    :ivar route_action_points_extensions: Additional proprietary
        information for the action points specified by the manufacturer
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_action_point: List[RouteActionPoint] = field(
        default_factory=list,
        metadata={
            "name": "routeActionPoint",
            "type": "Element",
            "namespace": "",
        },
    )
    route_action_points_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeActionPointsExtensions",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RouteWaypoint(AbstractFeatureType):
    """
    :ivar geometry: Geographical position of the waypoint in degrees
    :ivar route_waypoint_name: Name of waypoint
    :ivar route_waypoint_leg:
    :ivar route_schedule_element: The schedule elements for the
        waypoint. May be one of each types.
    :ivar route_waypoint_extensions: Additional proprietary information
        for the route waypoint specified by the manufacturer
    :ivar route_waypoint_id: Numeric identifier of waypoint. Shall be
        unique in the route.
    :ivar route_waypoint_external_reference_id: External reference
        information related with the waypoint
    :ivar route_waypoint_fixed: Indicator if the route waypoint is
        fixed(true) or editable(false)
    :ivar route_waypoint_turn_radius: Turn radius in nautical miles
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    geometry: Optional[GmPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    route_waypoint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeWaypointName",
            "type": "Element",
            "namespace": "",
        },
    )
    route_waypoint_leg: Optional[RouteWaypointLeg] = field(
        default=None,
        metadata={
            "name": "routeWaypointLeg",
            "type": "Element",
            "namespace": "",
        },
    )
    route_schedule_element: List[RouteScheduleElement] = field(
        default_factory=list,
        metadata={
            "name": "routeScheduleElement",
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
        },
    )
    route_waypoint_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeWaypointExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_waypoint_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeWaypointID",
            "type": "Attribute",
        },
    )
    route_waypoint_external_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeWaypointExternalReferenceID",
            "type": "Attribute",
        },
    )
    route_waypoint_fixed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "routeWaypointFixed",
            "type": "Attribute",
        },
    )
    route_waypoint_turn_radius: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "routeWaypointTurnRadius",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("5.00"),
            "fraction_digits": 2,
        },
    )


@dataclass
class MultiPointType2(MultiPointType1):
    """
    S-100 multipoint type adds an information association to the GML spatial type
    MultiPoint.
    """

    class Meta:
        name = "MultiPointType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class S100ArcByCenterPoint(S100ArcByCenterPointType):
    """This variant of the arc requires that the points on the arc shall be
    computed instead of storing the coordinates directly.

    The single control point is the center point of the arc. The other
    parameters are the radius, the bearing at start, and the angle from
    the start to the end relative to the center of the arc. This
    representation can be used only in 2D. The element radius specifies
    the radius of the arc. The element startAngle specifies the bearing
    of the arc at the start. The element angularDistance specifies the
    difference in bearing from the start to the end. The sign of
    angularDistance specifies the direction of the arc, positive values
    mean the direction is clockwise from start to end looking down from
    a point vertically above the center of the arc. Drawing starts at a
    bearing of 0.0 from the ray pointing due north from the center. If
    the center is at a pole the reference direction follows the prime
    meridian starting from the pole. The interpolation is fixed as
    "circularArcCenterPointWithRadius". Since this type always describes
    a single arc, the GML attribute "numArc" is not used.
    """

    class Meta:
        name = "S100_ArcByCenterPoint"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class S100CircleByCenterPointType(S100ArcByCenterPointType):
    class Meta:
        name = "S100_CircleByCenterPointType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    start_angle: Decimal = field(
        default=Decimal("0.0"),
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        },
    )
    angular_distance: S100CircleByCenterPointTypeAngularDistance = field(
        default=S100CircleByCenterPointTypeAngularDistance.VALUE_360_0,
        metadata={
            "name": "angularDistance",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )


@dataclass
class S100GmCurve(S100GmCurveType):
    """<xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Curve segments with other interpolations</xs:documentation>"""

    class Meta:
        name = "S100_GM_Curve"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class S100GmPolynomialSplineType(S100GmSplineCurveType):
    """<xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for polynomial splines</xs:documentation>"""

    class Meta:
        name = "S100_GM_PolynomialSplineType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    derivative_at_start: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "derivativeAtStart",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    derivative_at_end: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "derivativeAtEnd",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    num_derivative_interior: Optional[int] = field(
        default=None,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "required": True,
        },
    )


@dataclass
class S100GmSplineCurve(S100GmSplineCurveType):
    class Meta:
        name = "S100_GM_SplineCurve"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class GeodesicString(GeodesicStringType):
    """A sequence of geodesic segments.

    The number of control points shall be at least two. interpolation is
    fixed as "geodesic". The content model follows the general pattern
    for the encoding of curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodesicType(GeodesicStringType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LineString(LineStringType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. The number of direct positions in the
    list shall be at least two.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringSegment(LineStringSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    control points including the start and end point, with linear interpolation
    between them.

    The content model follows the general pattern for the encoding of
    curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRing(LinearRingType):
    """A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates shall be coincident.

    The number of direct positions in the list shall be at least four.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPoint1(MultiPointType1):
    """A gml:MultiPoint consists of one or more gml:Points.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:pointMember) or the array property
    (gml:pointMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """

    class Meta:
        name = "MultiPoint"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RouteWaypoints(AbstractFeatureType):
    """
    :ivar route_waypoint:
    :ivar route_waypoints_extensions: Additional proprietary information
        for the waypoints specified by the manufacturer
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_waypoint: List[RouteWaypoint] = field(
        default_factory=list,
        metadata={
            "name": "routeWaypoint",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        },
    )
    route_waypoints_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeWaypointsExtensions",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class MultiPoint2(MultiPointType2):
    class Meta:
        name = "MultiPoint"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class S100CircleByCenterPoint(S100CircleByCenterPointType):
    """An S100_CircleByCenterPoint is an S100_ArcByCenterPoint with angular
    distance +/- 360.0 degrees to form a full circle.

    Angular distance is assumed to be +360.0 degrees if it is missing.
    The interpolation is fixed as "circularArcCenterPointWithRadius".
    This representation can be used only in 2D.
    """

    class Meta:
        name = "S100_CircleByCenterPoint"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class S100GmPolynomialSpline(S100GmPolynomialSplineType):
    class Meta:
        name = "S100_GM_PolynomialSpline"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRingPropertyType:
    """
    A property with the content model of gml:LinearRingPropertyType encapsulates a
    linear ring to represent a component of a surface boundary.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class Route(AbstractFeatureType):
    """Route files contain a number of waypoints, with optional attached schedules
    amd legs.

    You can add your own elements to the various extension sections of
    the route. Note that support for extensions is not required to
    consume the route.

    :ivar route_format_version: The version of this route format
    :ivar route_info:
    :ivar route_waypoints:
    :ivar route_action_points:
    :ivar route_extensions: Additional proprietary information for the
        route specified by the manufacturer.
    :ivar route_edition_no: Route Edition number
    :ivar route_id: Unique identifier of the route
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    route_format_version: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "routeFormatVersion",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    route_info: Optional[RouteInfo] = field(
        default=None,
        metadata={
            "name": "routeInfo",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    route_waypoints: Optional[RouteWaypoints] = field(
        default=None,
        metadata={
            "name": "routeWaypoints",
            "type": "Element",
            "namespace": "",
        },
    )
    route_action_points: Optional[RouteActionPoints] = field(
        default=None,
        metadata={
            "name": "routeActionPoints",
            "type": "Element",
            "namespace": "",
        },
    )
    route_extensions: List[RouteExtensions] = field(
        default_factory=list,
        metadata={
            "name": "routeExtensions",
            "type": "Element",
            "namespace": "",
        },
    )
    route_edition_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "routeEditionNo",
            "type": "Attribute",
            "required": True,
        },
    )
    route_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeID",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MultiPointPropertyType(S100SpatialAttributeType):
    """
    MultiPoint property using the S-100 multipoint type.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    multi_point: Optional[MultiPoint2] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class CurveSegmentArrayPropertyType:
    """
    Gml:CurveSegmentArrayPropertyType is a container for an array of curve
    segments.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    s100_gm_curve: List[S100GmCurve] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "sequence": 1,
        },
    )
    s100_gm_polynomial_spline: List[S100GmPolynomialSpline] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_PolynomialSpline",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "sequence": 1,
        },
    )
    s100_gm_spline_curve: List[S100GmSplineCurve] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_SplineCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "sequence": 1,
        },
    )
    s100_circle_by_center_point: List[S100CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "S100_CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "sequence": 1,
        },
    )
    s100_arc_by_center_point: List[S100ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "S100_ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
            "sequence": 1,
        },
    )
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )


@dataclass
class ThisDatasetType(AbstractFeatureTypeAbstract):
    """
    :ivar dataset_identification_information: Dataset identification
        information
    :ivar route:
    """

    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    dataset_identification_information: Optional[DataSetIdentificationType] = (
        field(
            default=None,
            metadata={
                "name": "DatasetIdentificationInformation",
                "type": "Element",
                "namespace": "",
            },
        )
    )
    route: Optional[Route] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Dataset(ThisDatasetType):
    class Meta:
        name = "dataset"
        namespace = "http://www.iho.int/S421/gml/cs0/2.0"


@dataclass
class CurveType1(AbstractCurveType):
    class Meta:
        name = "CurveType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class CurveType2(CurveType1):
    """
    S-100 curve type adds an information association to the GML spatial type Curve.
    """

    class Meta:
        name = "CurveType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class Curve1(CurveType1):
    """A curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive. The element segments
    encapsulates the segments of the curve.
    """

    class Meta:
        name = "Curve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GmCurve:
    class Meta:
        name = "GM_Curve"
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    curve: Optional[CurveType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Curve2(CurveType2):
    class Meta:
        name = "Curve"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class CurvePropertyType1:
    """A property that has a curve as its value domain may either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    class Meta:
        name = "CurvePropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    orientable_curve: Optional["OrientableCurve2"] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    composite_curve: Optional["CompositeCurve2"] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_composite_curve: Optional["CompositeCurve1"] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_orientable_curve: Optional["OrientableCurve1"] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BaseCurve(CurvePropertyType1):
    """The property baseCurve references or contains the base curve, i.e. it either
    references the base curve via the XLink-attributes or contains the curve
    element.

    A curve element is any element which is substitutable for
    AbstractCurve. The base curve has positive orientation.
    """

    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveMember(CurvePropertyType1):
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeCurveType1(AbstractCurveType):
    class Meta:
        name = "CompositeCurveType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class OrientableCurveType(AbstractCurveType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    base_curve: Optional[BaseCurve] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RingType(AbstractRingType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class CompositeCurveType2(CompositeCurveType1):
    """
    S-100 composite curve type adds an information association to the GML spatial
    type CompositeCurve.
    """

    class Meta:
        name = "CompositeCurveType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class OrientableCurve2(OrientableCurveType):
    """S-100 orientable curve is the same as GML orientable curve.

    Added for consistency.
    """

    class Meta:
        name = "OrientableCurve"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class CompositeCurve1(CompositeCurveType1):
    """A gml:CompositeCurve is represented by a sequence of (orientable) curves
    such that each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    curveMember references or contains inline one curve in the composite
    curve. The curves are contiguous, the collection of curves is
    ordered. Therefore, if provided, the aggregationType attribute shall
    have the value "sequence".
    """

    class Meta:
        name = "CompositeCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableCurve1(OrientableCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another AbstractCurve with a parameterization that
    reverses the sense of the curve traversal.
    """

    class Meta:
        name = "OrientableCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Ring(RingType):
    """A ring is used to represent a single connected component of a surface
    boundary as specified in ISO 19107:2003, 6.3.6.

    Every gml:curveMember references or contains one curve, i.e. any
    element which is substitutable for gml:AbstractCurve. In the context
    of a ring, the curves describe the boundary of the surface. The
    sequence of curves shall be contiguous and connected in a cycle. If
    provided, the aggregationType attribute shall have the value
    "sequence".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeCurve2(CompositeCurveType2):
    class Meta:
        name = "CompositeCurve"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType encapsulates
    a ring to represent the surface boundary property of a surface.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class CurvePropertyType2(S100SpatialAttributeType):
    """
    Curve property using the S-100 curve type.
    """

    class Meta:
        name = "CurvePropertyType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    composite_curve: Optional[CompositeCurve2] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    orientable_curve: Optional[OrientableCurve2] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class Exterior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    In the normal 2D case, one of these rings is distinguished as being
    the exterior boundary. In a general manifold this is not always
    possible, in which case all boundaries shall be listed as interior
    boundaries, and the exterior will be empty.
    """

    class Meta:
        name = "exterior"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Interior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    The "interior" rings separate the surface / surface patch from the
    area enclosed by the rings.
    """

    class Meta:
        name = "interior"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveProperty(CurvePropertyType2):
    class Meta:
        name = "curveProperty"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PolygonType1(AbstractSurfaceType):
    class Meta:
        name = "PolygonType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class PolygonType2(PolygonType1):
    """
    S-100 polygon type adds an information association to the GML spatial type
    Polygon.
    """

    class Meta:
        name = "PolygonType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class PolygonPatch(PolygonPatchType):
    """A gml:PolygonPatch is a surface patch that is defined by a set of boundary
    curves and an underlying surface to which these curves adhere.

    The curves shall be coplanar and the polygon uses planar
    interpolation in its interior. interpolation is fixed to "planar",
    i.e. an interpolation shall return points on a single plane. The
    boundary of the patch shall be contained within that plane.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Polygon1(PolygonType1):
    """A Polygon is a special surface that is defined by a single surface patch
    (see D.3.6).

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. The elements exterior and interior
    describe the surface boundary of the polygon.
    """

    class Meta:
        name = "Polygon"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Polygon2(PolygonType2):
    """
    S100 version of polygon type.
    """

    class Meta:
        name = "Polygon"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    Gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class PolygonPropertyType:
    """
    Polygon property using the S-100 polygon type.
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """The patches property element contains the sequence of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonProperty(PolygonPropertyType):
    class Meta:
        name = "polygonProperty"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class SurfaceType1(AbstractSurfaceType):
    class Meta:
        name = "SurfaceType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class SurfaceType2(SurfaceType1):
    """
    S-100 surface type adds an information association to the GML spatial type
    Surface.
    """

    class Meta:
        name = "SurfaceType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class Surface1(SurfaceType1):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """

    class Meta:
        name = "Surface"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GmSurface:
    class Meta:
        name = "GM_Surface"
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    surface: Optional[SurfaceType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class RouteActionPointSpaceGeometry:
    class Meta:
        target_namespace = "http://www.iho.int/S421/gml/cs0/2.0"

    point: Optional[PointType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    curve: Optional[CurveType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    surface: Optional[SurfaceType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Surface2(SurfaceType2):
    class Meta:
        name = "Surface"
        namespace = "http://www.iho.int/s100gml/5.0"


@dataclass
class DatasetType(AbstractFeatureTypeAbstract):
    """
    Dataset element for dataset as "GML document".

    :ivar dataset_identification_information: Dataset identification
        information
    :ivar point:
    :ivar multi_point:
    :ivar curve:
    :ivar composite_curve:
    :ivar orientable_curve:
    :ivar surface:
    :ivar polygon:
    """

    class Meta:
        target_namespace = "http://www.iho.int/s100gml/5.0"

    dataset_identification_information: Optional[DataSetIdentificationType] = (
        field(
            default=None,
            metadata={
                "name": "DatasetIdentificationInformation",
                "type": "Element",
                "namespace": "http://www.iho.int/s100gml/5.0",
                "required": True,
            },
        )
    )
    point: List[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    multi_point: List[MultiPoint2] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    composite_curve: List[CompositeCurve2] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    orientable_curve: List[OrientableCurve2] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    surface: List[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    polygon: List[Polygon2] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class SurfacePropertyType2(S100SpatialAttributeType):
    """
    Surface property using the S-100 surface type.
    """

    class Meta:
        name = "SurfacePropertyType"
        target_namespace = "http://www.iho.int/s100gml/5.0"

    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )


@dataclass
class GeometricPrimitivePropertyType:
    """A property that has a geometric primitive as its value domain may either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon1] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_curve: Optional[OrientableCurve2] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    composite_curve: Optional[CompositeCurve2] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_composite_curve: Optional[CompositeCurve1] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_orientable_curve: Optional[OrientableCurve1] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )


@dataclass
class SurfacePropertyType1:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    class Meta:
        name = "SurfacePropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/5.0",
        },
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon1] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SurfaceProperty(SurfacePropertyType2):
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.iho.int/s100gml/5.0"
