/*
 * Copyright (c) 2008 Kasper Nielsen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package dma.dk.baleen.s124.utils;

import java.util.List;

import _int.iho.s124._1.Dataset;
import _int.iho.s124.s100.gml.profiles._5_0.AbstractGMLType;
import jakarta.xml.bind.JAXBException;

/**
 *
 */
public class Tester {
    public static final String DD = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<S124:Dataset xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:S124="http://www.iho.int/S124/1.0" xmlns:S100="http://www.iho.int/s100gml/5.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.iho.int/S124/gml/1.0 ./S100Defs/S124.xsd" gml:id="NW.CA.CCG.N.1814.22">
    <S100:DatasetIdentificationInformation>
        <S100:encodingSpecification>S-100 Part 10b</S100:encodingSpecification>
        <S100:encodingSpecificationEdition>1.0</S100:encodingSpecificationEdition>
        <S100:productIdentifier>S-124</S100:productIdentifier>
        <S100:productEdition>1.0.0</S100:productEdition>
        <S100:applicationProfile>Active NAVWARNs</S100:applicationProfile>
        <S100:datasetFileIdentifier>124CAN_1814_22.XML</S100:datasetFileIdentifier>
        <S100:datasetTitle>Seasonal Buoy Program</S100:datasetTitle>
        <S100:datasetReferenceDate>2022-12-02</S100:datasetReferenceDate>
        <S100:datasetLanguage>eng</S100:datasetLanguage>
        <S100:datasetAbstract>The abstract of the dataset</S100:datasetAbstract>
        <S100:datasetTopicCategory>oceans</S100:datasetTopicCategory>
        <S100:datasetPurpose>base</S100:datasetPurpose>
        <S100:updateNumber>0</S100:updateNumber>
    </S100:DatasetIdentificationInformation>
    <S124:members>
        <S124:NAVWARNPreamble gml:id="NW.CA.CCG.N.1814.22.0">
            <S124:affectedChartPublications>
                <S124:chartAffected>
                    <S124:chartNumber>4430</S124:chartNumber>
                    <S124:editionDate>2017-12-10</S124:editionDate>
                </S124:chartAffected>
                <S124:language>eng</S124:language>
                <S124:publicationAffected>Plans - Île D'Anticosti</S124:publicationAffected>
            </S124:affectedChartPublications>
            <S124:affectedChartPublications>
                <S124:chartAffected>
                    <S124:chartNumber>4722</S124:chartNumber>
                    <S124:editionDate>2021-08-12</S124:editionDate>
                </S124:chartAffected>
                <S124:language>eng</S124:language>
                <S124:publicationAffected>Terrington Basin</S124:publicationAffected>
            </S124:affectedChartPublications>
            <S124:generalArea>
                <S124:locationName>
                    <S124:language>eng</S124:language>
                    <S124:text>Newfoundland</S124:text>
                </S124:locationName>
            </S124:generalArea>
            <S124:generalArea>
                <S124:locationName>
                    <S124:language>eng</S124:language>
                    <S124:text>Labrador</S124:text>
                </S124:locationName>
            </S124:generalArea>
            <S124:messageSeriesIdentifier>
                <S124:agencyResponsibleForProduction>Canadian Coast Guard</S124:agencyResponsibleForProduction>
                <S124:countryName>Canada</S124:countryName>
                <S124:nameOfSeries>N</S124:nameOfSeries>
                <S124:warningIdentifier>urn:mrn:NW.CA.CCG.N.1814.22</S124:warningIdentifier>
                <S124:warningNumber>1814</S124:warningNumber>
                <S124:warningType code="1">Local Navigational Warning</S124:warningType>
                <S124:year>2022</S124:year>
            </S124:messageSeriesIdentifier>
            <S124:nAVWARNTitle>
                <S124:language>eng</S124:language>
                <S124:text>Seasonal Buoy Program</S124:text>
            </S124:nAVWARNTitle>
            <S124:intService>true</S124:intService>
            <S124:navwarnTypeGeneral code="other">other: Seasonal Buoy Program</S124:navwarnTypeGeneral>
            <S124:publicationTime>2022-12-02T17:26:48</S124:publicationTime>
            <S124:theReferences xlink:href="#NW.CA.CCG.N.1814.22.1"/>
            <S124:theReferences xlink:href="#NW.CA.CCG.N.1814.22.2"/>
            <S124:theReferences xlink:href="#NW.CA.CCG.N.1814.22.3"/>
            <S124:theReferences xlink:href="#NW.CA.CCG.N.1814.22.4"/>
        </S124:NAVWARNPreamble>
        <S124:References gml:id="NW.CA.CCG.N.1814.22.1">
            <S124:messageSeriesIdentifier>
                <S124:agencyResponsibleForProduction>Canadian Coast Guard</S124:agencyResponsibleForProduction>
                <S124:countryName>Canada</S124:countryName>
                <S124:nameOfSeries>N</S124:nameOfSeries>
                <S124:warningIdentifier>urn:mrn:NW.CA.CCG.N.1384.21</S124:warningIdentifier>
                <S124:warningNumber>2021</S124:warningNumber>
                <S124:warningType code="1">Local Navigational Warning</S124:warningType>
                <S124:year>2021</S124:year>
            </S124:messageSeriesIdentifier>
            <S124:noMessageOnHand>false</S124:noMessageOnHand>
            <S124:referenceCategory code="1">Warning Cancellation</S124:referenceCategory>
        </S124:References>
        <S124:References gml:id="NW.CA.CCG.N.1814.22.2">
            <S124:messageSeriesIdentifier>
                <S124:agencyResponsibleForProduction>Canadian Coast Guard</S124:agencyResponsibleForProduction>
                <S124:countryName>Canada</S124:countryName>
                <S124:nameOfSeries>N</S124:nameOfSeries>
                <S124:warningIdentifier>urn:mrn:NW.CA.CCG.N.1813.22</S124:warningIdentifier>
                <S124:warningNumber>2022</S124:warningNumber>
                <S124:warningType code="1">Local Navigational Warning</S124:warningType>
                <S124:year>2022</S124:year>
            </S124:messageSeriesIdentifier>
            <S124:noMessageOnHand>false</S124:noMessageOnHand>
            <S124:referenceCategory code="1">Warning Cancellation</S124:referenceCategory>
        </S124:References>
        <S124:References gml:id="NW.CA.CCG.N.1814.22.3">
            <S124:messageSeriesIdentifier>
                <S124:agencyResponsibleForProduction>Canadian Coast Guard</S124:agencyResponsibleForProduction>
                <S124:countryName>Canada</S124:countryName>
                <S124:nameOfSeries>N</S124:nameOfSeries>
                <S124:warningIdentifier>urn:mrn:NW.CA.CCG.N.1721.22</S124:warningIdentifier>
                <S124:warningNumber>2022</S124:warningNumber>
                <S124:warningType code="1">Local Navigational Warning</S124:warningType>
                <S124:year>2022</S124:year>
            </S124:messageSeriesIdentifier>
            <S124:noMessageOnHand>false</S124:noMessageOnHand>
            <S124:referenceCategory code="1">Warning Cancellation</S124:referenceCategory>
        </S124:References>
        <S124:NAVWARNPart gml:id="NW.CA.CCG.N.1814.22.4">
            <S124:fixedDateRange>
                <S124:dateStart>
                    <S100:date>2022-12-02</S100:date>
                </S124:dateStart>
            </S124:fixedDateRange>
            <S124:warningInformation>
                <S124:information>
                    <S124:language>eng</S124:language>
                    <S124:text>The seasonal decommissioning of Canadian Coast Guard navigational buoys is underway in : &lt;br /&gt;Newfoundland &lt;br /&gt;Labrador.</S124:text>
                </S124:information>
                <S124:navwarnTypeDetails code="other">other: Seasonal Buoy Lifting</S124:navwarnTypeDetails>
            </S124:warningInformation>
            <S124:header xlink:href="#NW.CA.CCG.N.1814.22.0"/>
            <S124:geometry>
                <S100:surfaceProperty>
                    <S100:Surface gml:id="NW.CA.CCG.N.1814.22.location.0" srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
                        <gml:patches>
                            <gml:PolygonPatch interpolation="planar">
<gml:exterior>
    <gml:LinearRing>
        <gml:posList srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2" count="22">-65.749033 60.068567 -65.486883 60.952533 -64.924100 62.375700 -64.289400 62.956533 -52.428317 63.013650 -47.800167 58.716900 -47.176867 57.655433 -50.527233 55.706133 -49.220317 53.433800 -53.997600 53.509750 -53.997667 52.499550 -54.188817 51.911617 -54.689100 51.548433 -56.010467 51.471017 -56.799067 51.614083 -57.528450 52.333317 -58.313033 52.873783 -61.086134 53.008811 -61.866750 54.864283 -63.775450 56.966150 -65.684850 59.633850 -65.749033 60.068567 </gml:posList>
    </gml:LinearRing>
</gml:exterior>
                            </gml:PolygonPatch>
                        </gml:patches>
                    </S100:Surface>
                </S100:surfaceProperty>
            </S124:geometry>
            <S124:geometry>
                <S100:surfaceProperty>
                    <S100:Surface gml:id="NW.CA.CCG.N.1814.22.location.1" srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
                        <gml:patches>
                            <gml:PolygonPatch interpolation="planar">
<gml:exterior>
    <gml:LinearRing>
        <gml:posList srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2" count="19">-61.543541 46.770557 -61.257549 47.861150 -61.499668 50.266137 -61.160182 51.051758 -57.245793 52.567618 -55.997597 53.465282 -55.949201 54.806763 -50.079641 55.109159 -45.872290 48.305462 -45.802425 47.432234 -46.755200 43.892699 -50.360049 41.663631 -55.038747 41.488812 -58.862031 41.009221 -59.773943 41.368813 -59.998232 41.999922 -59.998208 45.013594 -61.638580 46.003031 -61.543541 46.770557 </gml:posList>
    </gml:LinearRing>
</gml:exterior>
                            </gml:PolygonPatch>
                        </gml:patches>
                    </S100:Surface>
                </S100:surfaceProperty>
            </S124:geometry>
        </S124:NAVWARNPart>
    </S124:members>
</S124:Dataset>
                        """;

    public static final String TT2= "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ns4:Dataset xmlns:ns1=\"http://www.opengis.net/gml/3.2\" xmlns:ns2=\"http://www.iho.int/s100gml/5.0\" xmlns:ns3=\"http://www.w3.org/1999/xlink\" xmlns:ns4=\"http://www.iho.int/S124/1.0\" ns1:id=\"D\"><ns1:boundedBy><ns1:Envelope srsName=\"EPSG:4326\"><ns1:lowerCorner>54.6586333 10.6362500</ns1:lowerCorner><ns1:upperCorner>54.6586333 10.6362500</ns1:upperCorner></ns1:Envelope></ns1:boundedBy><ns2:Dataset\n";
    public static void main(String[] args) throws JAXBException {
        Dataset unmarshallS124 = S124Utils.unmarshallS124(TT2);


        List<? extends AbstractGMLType> l = S124Utils.getDatasetMembers(DD);

        System.out.println(l);
    }
}
