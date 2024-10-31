<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" encoding="UTF-8" indent="yes"/>
  <xsl:template match="NAVWARNAreaAffected[@primitive='Point']" priority="1">
    <pointInstruction>
      <featureReference>
        <xsl:value-of select="@id"/>
      </featureReference>
      <viewingGroup>12210</viewingGroup>
      <displayPlane>UNDERRADAR</displayPlane>
      <drawingPriority>15</drawingPriority>
      <symbol reference="NavigatoinalWarningFeaturePart">
      </symbol>
    </pointInstruction>
	  <!--  An augmented Path for the sector arc Local CRS -->
	  <augmentedPath>
		  <featureReference>
			  <xsl:value-of select="@id"/>
		  </featureReference>
		  <viewingGroup>27070</viewingGroup>
		  <displayPlane>OVERRADAR</displayPlane>
		  <drawingPriority>24</drawingPriority>
		  <crs>LocalCRS</crs>
		  <!-- add a linestlye element -->
		  <xsl:call-template name="simpleLineStyle">
			  <xsl:with-param name="style">dot</xsl:with-param>
			  <xsl:with-param name="width">0.32</xsl:with-param>
			  <xsl:with-param name="colour">OUTLW</xsl:with-param>
		  </xsl:call-template>
		  <path>
			  <arcByRadius>
				  <center>
					  <x>0</x>
					  <y>0</y>
				  </center>
				  <sector>
					  <startAngle>120</startAngle>
					  <angularDistance>30</angularDistance>
				  </sector>
				  <radius>30</radius>
			  </arcByRadius>
		  </path>
	  </augmentedPath>

	  <!--  An augmented ray for each sector leg with Local CRS -->
	  <augmentedRay>
		  <featureReference>
			  <xsl:value-of select="@id"/>
		  </featureReference>
		  <viewingGroup>12210</viewingGroup>
		  <displayPlane>UNDERRADAR</displayPlane>
		  <drawingPriority>15</drawingPriority>
		  <crs>LocalCRS</crs>
		  <!-- LocalCRS,  geographicCRS when using actual VALNMR-->
		  <!-- add a linestlye element -->
		  <xsl:call-template name="simpleLineStyle">
			  <xsl:with-param name="style">dot</xsl:with-param>
			  <xsl:with-param name="width">0.32</xsl:with-param>
			  <xsl:with-param name="colour">CHBLK</xsl:with-param>
		  </xsl:call-template>
		  <direction>
			  <!--  need to flip the bearing by 180 because values are seaward bearing-->
			  <xsl:value-of select="120"/>
		  </direction>
		  <!--  direction from sector limit +/- 180 -->
		  <length>
			  <xsl:value-of select="30"/>
		  </length>
		  <!--  Length fixed or nominal range -->
	  </augmentedRay>
	  <!--  An augmented ray for each sector leg with Local CRS -->
	  <augmentedRay>
		  <featureReference>
			  <xsl:value-of select="@id"/>
		  </featureReference>
		  <viewingGroup>12210</viewingGroup>
		  <displayPlane>UNDERRADAR</displayPlane>
		  <drawingPriority>15</drawingPriority>
		  <crs>LocalCRS</crs>
		  <!-- LocalCRS,  geographicCRS when using actual VALNMR-->
		  <!-- add a linestlye element -->
		  <xsl:call-template name="simpleLineStyle">	
			  <xsl:with-param name="style">dot</xsl:with-param>
			  <xsl:with-param name="width">0.32</xsl:with-param>
			  <xsl:with-param name="colour">CHBLK</xsl:with-param>
		  </xsl:call-template>
		  <direction>
			  <!--  need to flip the bearing by 180 because values are seaward bearing-->
			  <xsl:value-of select="150"/>
		  </direction>
		  <!--  direction from sector limit +/- 180 -->
		  <length>
			  <xsl:value-of select="30"/>
		  </length>
		  <!--  Length fixed or nominal range -->
	  </augmentedRay>

  </xsl:template>

</xsl:transform>
