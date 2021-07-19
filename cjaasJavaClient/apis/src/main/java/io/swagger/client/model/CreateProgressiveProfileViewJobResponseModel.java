/*
 * Azure Functions OpenAPI Extension
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * CreateProgressiveProfileViewJobResponseModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2021-07-06T08:57:46.449-05:00[America/Chicago]")
public class CreateProgressiveProfileViewJobResponseModel {
  @SerializedName("id")
  private String id = null;

  @SerializedName("getUriStatusQuery")
  private String getUriStatusQuery = null;

  public CreateProgressiveProfileViewJobResponseModel id(String id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @Schema(description = "")
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public CreateProgressiveProfileViewJobResponseModel getUriStatusQuery(String getUriStatusQuery) {
    this.getUriStatusQuery = getUriStatusQuery;
    return this;
  }

   /**
   * Get getUriStatusQuery
   * @return getUriStatusQuery
  **/
  @Schema(description = "")
  public String getGetUriStatusQuery() {
    return getUriStatusQuery;
  }

  public void setGetUriStatusQuery(String getUriStatusQuery) {
    this.getUriStatusQuery = getUriStatusQuery;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateProgressiveProfileViewJobResponseModel createProgressiveProfileViewJobResponseModel = (CreateProgressiveProfileViewJobResponseModel) o;
    return Objects.equals(this.id, createProgressiveProfileViewJobResponseModel.id) &&
        Objects.equals(this.getUriStatusQuery, createProgressiveProfileViewJobResponseModel.getUriStatusQuery);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, getUriStatusQuery);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateProgressiveProfileViewJobResponseModel {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    getUriStatusQuery: ").append(toIndentedString(getUriStatusQuery)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}